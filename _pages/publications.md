---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
redirect_from:
  - /publications.html
---

{% include base_path %}

## Refereed Journal Articles

<ul>
{% assign journals = site.publications | where: "category", "journals" | sort: "date" | reverse %}
{% for pub in journals %}
  <li>
    {{ pub.citation }}
    {% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">[doi]</a>{% endif %}
  </li>
{% endfor %}
</ul>

## Refereed International Conference Papers

<ul>
{% assign confs = site.publications | where: "category", "conferences" | sort: "date" | reverse %}
{% for pub in confs %}
  <li>
    {{ pub.citation }}
  </li>
{% endfor %}
</ul>
