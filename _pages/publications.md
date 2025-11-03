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
</div>

{% include publications_by_year.html %}
