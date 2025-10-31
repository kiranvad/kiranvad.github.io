#!/usr/bin/env python3
"""
Google Scholar Stats Updater
Fetches citation statistics directly from the public Google Scholar profile
and updates the Jekyll data file. Falls back to scholarly/manually curated
values when scraping fails.
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Dict, Tuple

import requests
import yaml
from bs4 import BeautifulSoup

try:  # Optional fallback dependency
    from scholarly import scholarly  # type: ignore
except ImportError:  # pragma: no cover - scholarly may not be installed
    scholarly = None

SCHOLAR_ID = "GbNEbEkAAAAJ"
DATA_FILE = "_data/scholar_stats.yml"
PROFILE_URL = "https://scholar.google.com/citations"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

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


def parse_int(text: str) -> int:
    """Convert a string with commas/non-breaking spaces into an integer."""
    cleaned = text.replace(",", "").replace("\xa0", "").strip()
    return int(cleaned) if cleaned.isdigit() else 0


def fetch_via_requests() -> Tuple[Dict[str, int], Dict[int, int]]:
    """Scrape the public Google Scholar profile using requests + BeautifulSoup."""
    params = {"user": SCHOLAR_ID, "hl": "en"}
    headers = {"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}

    response = requests.get(PROFILE_URL, params=params, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    stats_table = soup.select_one("#gsc_rsb_st")
    if not stats_table:
        raise ValueError("Could not locate statistics table on Google Scholar profile page")

    stats_rows = stats_table.select("tr")
    metrics = ["total_citations", "h_index", "i10_index"]
    stats = {}

    for metric, row in zip(metrics, stats_rows):
        cells = row.select("td.gsc_rsb_std")
        if not cells:
            raise ValueError(f"Missing cell data for {metric}")
        stats[metric] = parse_int(cells[0].text)

    if len(stats) != len(metrics):
        raise ValueError("Incomplete statistics extracted from profile page")

    year_elements = soup.select("#gsc_rsb_cit span.gsc_g_t")
    count_elements = soup.select("#gsc_rsb_cit span.gsc_g_al")

    if not year_elements or not count_elements:
        raise ValueError("Could not locate citation histogram data on profile page")

    citations_by_year = {}
    for year_el, count_el in zip(year_elements, count_elements):
        year_text = year_el.text.strip()
        if not year_text.isdigit():
            continue
        citations_by_year[int(year_text)] = parse_int(count_el.text)

    if not citations_by_year:
        raise ValueError("No yearly citation data found while parsing profile page")

    citations_by_year = dict(sorted(citations_by_year.items()))
    return stats, citations_by_year


def fetch_via_scholarly() -> Tuple[Dict[str, int], Dict[int, int]]:
    """Fallback to the scholarly library when direct scraping is unavailable."""
    if scholarly is None:
        raise ImportError("scholarly is not installed")

    author = scholarly.search_author_id(SCHOLAR_ID)
    if not author:
        raise RuntimeError(f"Author with ID {SCHOLAR_ID} not found via scholarly")

    author = scholarly.fill(author, sections=["indices"])

    stats = {
        "total_citations": author.get("citedby", 0),
        "h_index": author.get("hindex", 0),
        "i10_index": author.get("i10index", 0),
    }

    citations_by_year = {
        int(year): count
        for year, count in author.get("cites_per_year", {}).items()
        if str(year).isdigit()
    }

    if not citations_by_year:
        raise ValueError("scholarly did not return yearly citation data")

    citations_by_year = dict(sorted(citations_by_year.items()))
    return stats, citations_by_year


def fetch_scholar_data() -> Tuple[Dict[str, int], Dict[int, int]]:
    """Attempt to fetch Scholar stats using multiple strategies."""
    try:
        print("Fetching Google Scholar data via direct scraping...")
        return fetch_via_requests()
    except Exception as direct_error:
        print(f"Primary scraping failed: {direct_error}")

    try:
        print("Falling back to scholarly library...")
        return fetch_via_scholarly()
    except Exception as scholarly_error:
        print(f"scholarly fallback failed: {scholarly_error}")

    print("Falling back to manually curated citation data")
    return FALLBACK_STATS, FALLBACK_CITATIONS_BY_YEAR


def update_data_file(stats: Dict[str, int], citations_by_year: Dict[int, int]) -> bool:
    """Persist the fetched statistics into the YAML data file."""
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
        print(f"Error writing data file: {write_error}")
        return False


def main() -> int:
    print("Starting Google Scholar stats update...")
    stats, citations_by_year = fetch_scholar_data()

    if not stats or not citations_by_year:
        print("Failed to retrieve Google Scholar data")
        return 1

    if update_data_file(stats, citations_by_year):
        print("Google Scholar stats updated successfully!")
        return 0

    print("Failed to update Google Scholar stats")
    return 1


if __name__ == "__main__":
    sys.exit(main())
