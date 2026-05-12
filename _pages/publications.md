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
    {% if pub.paperurl %} <a href="{{ pub.paperurl }}">[pdf]</a>{% endif %}
    <a href="{{ pub.url }}">[link]</a>
  </li>
{% endfor %}
</ul>

## Refereed International Conference Papers

<ul>
{% assign confs = site.publications | where: "category", "conferences" | sort: "date" | reverse %}
{% for pub in confs %}
  <li>
    {{ pub.citation }}
    {% if pub.paperurl %} <a href="{{ pub.paperurl }}">[pdf]</a>{% endif %}
    <a href="{{ pub.url }}">[link]</a>
  </li>
{% endfor %}
</ul>
