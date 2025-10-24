---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign scholar = site.data.scholar_stats %}

<div class="scholar-section">

  <!-- Google Scholar Stats -->
  <h2>Google Scholar Statistics</h2>
  <div class="scholar-stats-container">
    <div class="scholar-stats-grid">
      <div class="stat-card">
        <div class="stat-number">{{ scholar.total_citations }}</div>
        <div class="stat-label">Total Citations</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">{{ scholar.h_index }}</div>
        <div class="stat-label">h-index</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">{{ scholar.i10_index }}</div>
        <div class="stat-label">i10-index</div>
      </div>
    </div>
    
    <div class="citation-chart-container">
      <canvas id="citation-chart" 
              data-citations='{{ scholar.citations_by_year | jsonify }}'
              width="400" 
              height="200">
      </canvas>
    </div>
    
    <div class="scholar-link">
      <p><a href="{{ scholar.profile_url }}" target="_blank" rel="noopener">View full profile on Google Scholar</a></p>
      <small>Last updated: {{ scholar.last_updated }}</small>
    </div>
  </div>

  <!-- Publications Tabs -->
  <div class="tabs-container">

    <!-- Tabs -->
    <ul class="tabs">
      {% assign years = site.data.publications | map: "year" | uniq | sort: "reverse" %}
      {% for year in years %}
        <li class="tab" data-year="{{ year }}">{{ year }}</li>
      {% endfor %}
    </ul>

    <!-- Tab Contents -->
    {% for year in years %}
      <div class="tab-content" id="year-{{ year }}">
        {% assign pubs = site.data.publications | where: "year", year %}
        {% for pub in pubs %}
          <p>
            <strong>{{ pub.title }}</strong>, {{ pub.journal }}, {{ pub.year }}.<br>
            Authors: {{ pub.authors }}.<br>
            {% if pub.code %}[<a href="{{ pub.code }}">Code</a>]{% endif %}
            {% if pub.data %}[<a href="{{ pub.data }}">Data</a>]{% endif %}
          </p>
        {% endfor %}
      </div>
    {% endfor %}

  </div> <!-- end tabs-container -->
</div> <!-- end scholar-section -->

<script>
document.addEventListener("DOMContentLoaded", function() {
  const tabs = document.querySelectorAll(".tab");
  const contents = document.querySelectorAll(".tab-content");

  tabs.forEach(tab => {
    tab.addEventListener("click", function() {
      tabs.forEach(t => t.classList.remove("active"));
      contents.forEach(c => c.classList.remove("active"));

      tab.classList.add("active");
      const year = tab.dataset.year;
      document.getElementById("year-" + year).classList.add("active");
    });
  });

  // Activate the first tab by default
  if(tabs.length > 0) {
    tabs[0].click();
  }
});
</script>
