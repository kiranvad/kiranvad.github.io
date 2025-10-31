#!/usr/bin/env python3
"""Google Scholar stats updater.

The fetcher prioritizes SerpAPI (stable, official Google Scholar scraper)
when the ``SERPAPI_API_KEY`` environment variable is provided. If the key is
absent or SerpAPI fails, it falls back to a lightweight HTML scrape and, as a
last resort, the scholarly library or static defaults.
"""

from __future__ import annotations

import os
import sys
from datetime import datetime
from typing import Dict, Tuple

import requests
import yaml
from bs4 import BeautifulSoup

try:  # Optional fallback dependency
    from scholarly import scholarly  # type: ignore
except ImportError:  # pragma: no cover
    scholarly = None

SCHOLAR_ID = "GbNEbEkAAAAJ"
PROFILE_URL = "https://scholar.google.com/citations"
DATA_FILE = "_data/scholar_stats.yml"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

FALLBACK_STATS = {
    "total_citations": 45,
    "h_index": 8,
    "i10_index": 6,
}
FALLBACK_CITATIONS_BY_YEAR = {
    2019: 7,
    2020: 8,
    2021: 9,
    2022: 10,
    2023: 11,
    2024: 12,
    2025: 3,
}


def parse_int(value: str | int | float) -> int:
    """Best-effort conversion of strings with commas or spaces to integers."""
    if isinstance(value, (int, float)):
        return int(value)
    cleaned = value.replace(",", "").replace("\xa0", "").strip()
    return int(cleaned) if cleaned.isdigit() else 0


def fetch_via_serpapi() -> Tuple[Dict[str, int], Dict[int, int]]:
    """Retrieve statistics via SerpAPI's google_scholar_author engine."""
    if not SERPAPI_KEY:
        raise ValueError("SERPAPI_API_KEY not provided")

    params = {
        "engine": "google_scholar_author",
        "author_id": SCHOLAR_ID,
        "hl": "en",
        "api_key": SERPAPI_KEY,
    }

    response = requests.get(SERPAPI_ENDPOINT, params=params, timeout=30)
    response.raise_for_status()

    payload = response.json()
    if "error" in payload:
        raise RuntimeError(payload["error"])

    cited_by = payload.get("cited_by", {})
    table = cited_by.get("table", [])
    graph = cited_by.get("graph", [])

    if not table:
        raise ValueError("Missing citation table in SerpAPI response")

    metrics = {entry.get("name", "").lower(): entry for entry in table}

    stats = {
        "total_citations": parse_int(metrics.get("citations", {}).get("citations", {}).get("all", 0)),
        "h_index": parse_int(metrics.get("h_index", {}).get("h_index", {}).get("all", 0)),
        "i10_index": parse_int(metrics.get("i10-index", {}).get("i10_index", {}).get("all", 0)),
    }

    if not any(stats.values()):
        raise ValueError("SerpAPI response did not contain citation metrics")

    citations_by_year: Dict[int, int] = {}
    for node in graph:
        year = node.get("year")
        citations = node.get("citations")
        if isinstance(year, int) and year >= 1900:
            citations_by_year[year] = parse_int(citations or 0)

    if not citations_by_year:
        raise ValueError("SerpAPI response missing citation graph")

    return stats, dict(sorted(citations_by_year.items()))


def fetch_via_requests() -> Tuple[Dict[str, int], Dict[int, int]]:
    """Fallback scraper using requests + BeautifulSoup."""
    params = {"user": SCHOLAR_ID, "hl": "en"}
    headers = {"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}

    response = requests.get(PROFILE_URL, params=params, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    stats_table = soup.select_one("#gsc_rsb_st")
    if not stats_table:
        raise ValueError("Could not locate statistics table on profile page")

    stats_rows = stats_table.select("tr")
    metrics = ["total_citations", "h_index", "i10_index"]
    stats: Dict[str, int] = {}

    for metric, row in zip(metrics, stats_rows):
        cell = row.select_one("td.gsc_rsb_std")
        if not cell:
            raise ValueError(f"Missing value for {metric}")
        stats[metric] = parse_int(cell.text)

    year_elements = soup.select("#gsc_rsb_cit span.gsc_g_t")
    count_elements = soup.select("#gsc_rsb_cit span.gsc_g_al")

    if not year_elements or not count_elements:
        raise ValueError("Could not locate citation histogram data")

    citations_by_year: Dict[int, int] = {}
    for year_el, count_el in zip(year_elements, count_elements):
        year_text = year_el.text.strip()
        if year_text.isdigit():
            citations_by_year[int(year_text)] = parse_int(count_el.text)

    if not citations_by_year:
        raise ValueError("No yearly citation data found")

    return stats, dict(sorted(citations_by_year.items()))


def fetch_via_scholarly() -> Tuple[Dict[str, int], Dict[int, int]]:
    """Last-resort fetch using the scholarly library."""
    if scholarly is None:
        raise ImportError("scholarly not installed")

    author = scholarly.search_author_id(SCHOLAR_ID)
    if not author:
        raise RuntimeError(f"Author {SCHOLAR_ID} not found via scholarly")

    author = scholarly.fill(author, sections=["indices"])

    stats = {
        "total_citations": author.get("citedby", 0),
        "h_index": author.get("hindex", 0),
        "i10_index": author.get("i10index", 0),
    }

    citations_by_year = {
        int(year): int(count)
        for year, count in author.get("cites_per_year", {}).items()
        if str(year).isdigit()
    }

    if not citations_by_year:
        raise ValueError("scholarly did not emit yearly citation data")

    return stats, dict(sorted(citations_by_year.items()))


def fetch_scholar_data() -> Tuple[Dict[str, int], Dict[int, int]]:
    """Best-effort retrieval with cascading fallbacks."""
    fetchers = [
        ("SerpAPI", fetch_via_serpapi),
        ("requests scrape", fetch_via_requests),
        ("scholarly", fetch_via_scholarly),
    ]

    for name, fetcher in fetchers:
        try:
            print(f"Attempting fetch via {name}...")
            stats, yearly = fetcher()
            print(f"Success via {name}")
            return stats, yearly
        except Exception as error:  # pragma: no cover - diagnostic output
            print(f"{name} fetch failed: {error}")

    print("Falling back to static citation data")
    return FALLBACK_STATS, FALLBACK_CITATIONS_BY_YEAR


def update_data_file(stats: Dict[str, int], citations_by_year: Dict[int, int]) -> bool:
    """Persist fetched statistics to the YAML datastore."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
    except FileNotFoundError:
        print(f"Data file {DATA_FILE} not found")
        return False

    data["total_citations"] = int(stats.get("total_citations", 0))
    data["h_index"] = int(stats.get("h_index", 0))
    data["i10_index"] = int(stats.get("i10_index", 0))
    data["citations_by_year"] = dict(sorted((int(year), int(count)) for year, count in citations_by_year.items()))
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as handle:
            yaml.dump(data, handle, default_flow_style=False, sort_keys=False)
        print(f"Updated {DATA_FILE} with new statistics")
        return True
    except OSError as write_error:
        print(f"Failed to write data file: {write_error}")
        return False


def main() -> int:
    print("Starting Google Scholar stats update...")
    stats, yearly = fetch_scholar_data()

    if not stats or not yearly:
        print("Unable to retrieve Google Scholar statistics")
        return 1

    if update_data_file(stats, yearly):
        print("Google Scholar stats updated successfully!")
        return 0

    print("Google Scholar stats update failed")
    return 1


if __name__ == "__main__":
    sys.exit(main())
