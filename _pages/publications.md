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
.accordion {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.accordion input[type="checkbox"] {
  display: none;
}

.accordion label {
  flex: 1 1 80px;
  text-align: center;
  background-color: #007bff;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  user-select: none;
  transition: background 0.2s ease;
}

.accordion label:hover {
  background-color: #0056b3;
}

.accordion input[type="checkbox"]:checked + label {
  background-color: #0056b3;
}

.accordion .content {
  display: none;
  width: 100%;
  margin-top: 0.5rem;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
}

.accordion input[type="checkbox"]:checked + label + .content {
  display: block;
}
</style>

<div class="accordion">

  <!-- 2025 -->
  <input type="checkbox" id="pub2025">
  <label for="pub2025">2025</label>
  <div class="content">
    <ul>
      <li>
        <a href="https://chemrxiv.org/engage/chemrxiv/article-details/67930f56fa469535b99a0dd1">Autonomous Phase Mapping of Gold Nanoparticles Synthesis with Differentiable Models of Spectral Shape (2025)</a>
        <br><strong>Vaddi, Kiran</strong>, Huat Thart Chiang, and Lilo D. Pozzo.
        <blockquote>Accepted to be published in <em>npj Computational Materials</em> (October 2nd, 2025)</blockquote>
        <a href="https://github.com/pozzo-research-group/activephasemap"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
        <a href="https://github.com/pozzo-research-group/papers/tree/activephasemap-preprint/seed-AuNP-phasemaps"><img src="https://img.shields.io/badge/Data-Zenodo-orange?logo=zenodo"></a>
      </li>
      <li>
        <a href="https://doi.org/10.1107/S1600576725001201">Efficient analysis of small-angle scattering curves for large biomolecular assemblies using Monte Carlo methods</a>,
        <em>Journal of Applied Crystallography</em> 58 (3) (2025) Huat Thart Chiang, Zhiyin Zhang, <strong>Kiran Vaddi</strong>, F. Akif Tezcan, Lilo D. Pozzo.
        <br>
        <a href="https://github.com/pozzo-research-group/MC-DFM"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
      </li>
    </ul>
  </div>

  <!-- 2024 -->
  <input type="checkbox" id="pub2024">
  <label for="pub2024">2024</label>
  <div class="content">
    <ul>
      <li>
        <a href="https://doi.org/10.1021/acs.macromol.4c01814">Self-assembly of a Triblock Copolymer in the Presence of a Rigid Conjugated Polyelectrolyte</a>,
        <em>Macromolecules</em> 57 (24), 11717–11726 (2024) Karen Li, <strong>Kiran Vaddi</strong>, Soenke Seifert, Jitendra Mata, Lilo D. Pozzo. <br>
        <a href="https://github.com/pozzo-research-group/papers/tree/main/Silver%20Nanoplates"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
        <a href="https://github.com/pozzo-research-group/papers/tree/main/pluronic-phasemaps"><img src="https://img.shields.io/badge/Data-Zenodo-orange?logo=zenodo"></a>
      </li>
      <li>
        <a href="https://doi.org/10.1039/D4DD00131A">Data-driven exploration of silver nanoplate formation in multidimensional chemical design spaces</a>,
        <em>Digital Discovery</em> 3 (11), 2252–2264 (2024) Huat Thart Chiang, <strong>Kiran Vaddi</strong>, Lilo D. Pozzo. <br>
        <a href="https://github.com/pozzo-research-group/autophasemap"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
      </li>
    </ul>
  </div>

  <!-- 2023 -->
  <input type="checkbox" id="pub2023">
  <label for="pub2023">2023</label>
  <div class="content">
    <ul>
      <li>
        <a href="https://doi.org/10.1039/D3DD00052D">A high-throughput workflow for the synthesis of CdSe nanocrystals using a sonochemical materials acceleration platform</a>,
        <em>Digital Discovery</em> 2 (4), 1042–1057 (2023) Maria Politi et al. <strong>Kiran Vaddi</strong>.  
        <blockquote>RSC Digital Discovery’s Editor Choice Article</blockquote>
        <a href="https://github.com/pozzo-research-group/papers/tree/main/qdots"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
      </li>
      <li>
        <a href="https://doi.org/10.1039/D3DD00041A">Metric geometry tools for automatic structure phase map generation</a>,
        <em>Digital Discovery</em> 2 (5), 1471–1483 (2023) <strong>Kiran Vaddi</strong>, Karen Li, Lilo D. Pozzo. <br>
        <a href="https://github.com/pozzo-research-group/autophasemap"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
        <a href="https://github.com/pozzo-research-group/papers/tree/main/autophasemap"><img src="https://img.shields.io/badge/Data-Zenodo-orange?logo=zenodo"></a>
      </li>
      <li>
        <a href="https://doi.org/10.1016/j.commatsci.2022.111829">Construction and high throughput exploration of phase diagrams of multi-component organic blends</a>,
        <em>Computational Materials Science</em> 216, 111829 (2023) <strong>Kiran Vaddi</strong> et al.  
        <a href="https://github.com/kiranvad/polyphase"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
      </li>
    </ul>
  </div>

  <!-- 2022 -->
  <input type="checkbox" id="pub2022">
  <label for="pub2022">2022</label>
  <div class="content">
    <ul>
      <li>
        <a href="https://doi.org/10.1039/D2DD00025C">Autonomous retrosynthesis of gold nanoparticles via spectral shape matching</a>,
        <em>Digital Discovery</em> 1 (4), 502–510 (2022) <strong>Kiran Vaddi</strong>, Huat Thart Chiang, and Lilo D. Pozzo.
        <blockquote>RSC Digital Discovery’s Editor Choice Article. Introduces Amplitude-Phase Distance for Spectral Shape Measurements.</blockquote>
        <a href="https://github.com/pozzo-research-group/HEAD/tree/BO"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
        <a href="https://github.com/kiranvad/Amplitude-Phase-Distance"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
      </li>
      <li>
        <a href="https://doi.org/10.1039/D2DD00047D">Multivariate analysis of peptide-driven nucleation and growth of Au nanoparticles</a>,
        <em>Digital Discovery</em> 1 (4), 427–439 (2022) Lachowski, Kacper J., <strong>Kiran Vaddi</strong>, et al.  
        <a href="https://gist.github.com/kiranvad/a46af46cbb3a114b4ab2b1970ba9cfa5"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
        <a href="https://zenodo.org/record/6588769"><img src="https://img.shields.io/badge/Data-Zenodo-orange?logo=zenodo"></a>
      </li>
      <li>
        <a href="https://doi.org/10.3390/en15134575">Active knowledge extraction from cyclic voltammetry</a>,
        <em>Energies</em> 15 (13), 4575 (2022) <strong>Kiran Vaddi</strong> and Olga Wodo.  
        <a href="https://github.com/kiranvad/GPCV"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
      </li>
    </ul>
  </div>

  <!-- 2021 -->
  <input type="checkbox" id="pub2021">
  <label for="pub2021">2021</label>
  <div class="content">
    <ul>
      <li>
        <strong>Representations for Data-Driven Material Discovery</strong>, PhD Dissertation, SUNY Buffalo (2021) <strong>Kiran Vaddi</strong>.  
        <a href="https://github.com/kiranvad/PhDThesis"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
      </li>
    </ul>
  </div>

  <!-- 2020 -->
  <input type="checkbox" id="pub2020">
  <label for="pub2020">2020</label>  
  <div class="content">
  <ul>
    <li>
      <a href="https://doi.org/10.1007/978-981-15-2666-4_4">Reduction of Escape Cone Losses in Luminescent Solar Concentrators Using High-Contrast Gratings</a>,
      <em>Advances in Energy Research</em> Vol. 1, 37–43 (2020) Elikkottil, Athira, <strong>Kiran Vaddi</strong>, K. S. Reddy, Bala Pesala.
    </li>
  </ul>
  </div>

  <!-- 2019 -->
  <input type="checkbox" id="pub2019">
  <label for="pub2019">2019</label>  
  <div class="content">
    <ul>
      <li>
        <a href="https://doi.org/10.1021/acscombsci.9b00102">Metric learning for high-throughput combinatorial data sets</a>,
        <em>ACS Combinatorial Science</em> 21 (11), 726–735 (2019) <strong>Kiran Vaddi</strong> and Olga Wodo.  
        <a href="https://github.com/kiranvad/MLCD"><img src="https://img.shields.io/badge/Code-GitHub-blue?logo=github"></a>
      </li>
    </ul>
  </div>

</div>
