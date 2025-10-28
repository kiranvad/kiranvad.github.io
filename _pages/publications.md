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

<style>
.year-buttons {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 1rem;
  gap: 0.5rem;
}

.year-button {
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s ease;
}

.year-button.active {
  background-color: #007bff;
  color: white;
  border-color: #007bff;
}

.year-content {
  display: none;
  border-top: 1px solid #ccc;
  margin-top: 1rem;
  padding-top: 1rem;
}

.year-content.active {
  display: block;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.publications {
  max-width: 900px;
  margin: auto;
  line-height: 1.6;
}

.publications a {
  color: #007bff;
  text-decoration: none;
}

.publications a:hover {
  text-decoration: underline;
}
</style>

<div class="publications">
  <div class="year-buttons">
    <button class="year-button" data-year="2025">2025</button>
    <button class="year-button" data-year="2024">2024</button>
    <button class="year-button" data-year="2023">2023</button>
    <button class="year-button" data-year="2022">2022</button>
    <button class="year-button" data-year="2021">2021</button>
    <button class="year-button" data-year="2020">2020</button>
    <button class="year-button" data-year="2019">2019</button>
  </div>

  <!-- 2025 -->
  <div class="year-content" id="2025">
    <ul>
      <li>
        <a href="https://chemrxiv.org/engage/chemrxiv/article-details/67930f56fa469535b99a0dd1">Autonomous Phase Mapping of Gold Nanoparticles Synthesis with Differentiable Models of Spectral Shape (2025)</a><br>
        <strong>Vaddi, Kiran</strong>, Huat Thart Chiang, and Lilo D. Pozzo.<br>
        <em>Accepted to npj Computational Materials (Oct 2, 2025)</em><br>
        <a href="https://github.com/pozzo-research-group/activephasemap">[Code]</a>
        <a href="https://github.com/pozzo-research-group/papers/tree/activephasemap-preprint/seed-AuNP-phasemaps">[Data]</a>
      </li>
      <li>
        <a href="https://doi.org/10.1107/S1600576725001201">Efficient analysis of small-angle scattering curves...</a><br>
        Huat Thart Chiang, Zhiyin Zhang, <strong>Kiran Vaddi</strong>, F. A. Tezcan, L. D. Pozzo.<br>
        <em>Journal of Applied Crystallography, 2025</em><br>
        <a href="https://github.com/pozzo-research-group/MC-DFM">[Code]</a>
      </li>
    </ul>
  </div>

  <!-- 2024 -->
  <div class="year-content" id="2024">
    <ul>
      <li>
        <a href="https://doi.org/10.1021/acs.macromol.4c01814">Self-assembly of a Triblock Copolymer...</a><br>
        Karen Li, <strong>Kiran Vaddi</strong>, et al.<br>
        <em>Macromolecules 57 (24), 11717–11726 (2024)</em><br>
        <a href="https://github.com/pozzo-research-group/papers/tree/main/Silver%20Nanoplates">[Code]</a>
        <a href="https://github.com/pozzo-research-group/papers/tree/main/pluronic-phasemaps">[Data]</a>
      </li>
      <li>
        <a href="https://doi.org/10.1039/D4DD00131A">Data-driven exploration of silver nanoplate formation...</a><br>
        Huat Thart Chiang, <strong>Kiran Vaddi</strong>, and L. D. Pozzo.<br>
        <em>Digital Discovery 3 (11), 2252–2264 (2024)</em><br>
        <a href="https://github.com/pozzo-research-group/autophasemap">[Code]</a>
      </li>
    </ul>
  </div>

  <!-- 2023 -->
  <div class="year-content" id="2023">
    <ul>
      <li>
        <a href="https://doi.org/10.1039/D3DD00052D">A high-throughput workflow for the synthesis of CdSe nanocrystals...</a><br>
        Maria Politi, Fabio Baum, <strong>Kiran Vaddi</strong>, et al.<br>
        <em>Digital Discovery 2 (4), 1042–1057 (2023)</em>
      </li>
      <li>
        <a href="https://doi.org/10.1039/D3DD00041A">Metric geometry tools for automatic structure phase map generation</a><br>
        <strong>Kiran Vaddi</strong>, Karen Li, and L. D. Pozzo.<br>
        <em>Digital Discovery 2 (5), 1471–1483 (2023)</em>
      </li>
      <li>
        <a href="https://doi.org/10.1016/j.commatsci.2022.111829">Construction and high throughput exploration...</a><br>
        <strong>Kiran Vaddi</strong>, H. Liu, B. Pokuri, B. Ganapathysubramanian, O. Wodo.<br>
        <em>Computational Materials Science 216, 111829 (2023)</em>
      </li>
    </ul>
  </div>

  <!-- Add remaining years 2022–2019 similarly -->
</div>

<script>
document.querySelectorAll('.year-button').forEach(button => {
  button.addEventListener('click', () => {
    const year = button.getAttribute('data-year');
    const content = document.getElementById(year);

    const isActive = button.classList.contains('active');

    // Reset all
    document.querySelectorAll('.year-button').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.year-content').forEach(div => div.classList.remove('active'));

    // Toggle
    if (!isActive) {
      button.classList.add('active');
      content.classList.add('active');
    }
  });
});
</script>