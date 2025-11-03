---
layout: archive
title: ""
permalink: /talks/
author_profile: true
---

{% assign invited_talks = site.data.talks | where: "type", "invited" %}
{% assign contributed_talks = site.data.talks | where: "type", "contributed" %}

Invited Talks
=====

<div class="talks-section">
  {% include talks_by_year.html talks=invited_talks tab_group="invited-talks" tab_prefix="invited-" aria_label="Invited talks by year" %}
</div>

Contributed Talks
=====

<div class="talks-section">
  {% include talks_by_year.html talks=contributed_talks tab_group="contributed-talks" tab_prefix="contributed-" aria_label="Contributed talks by year" %}
</div>
