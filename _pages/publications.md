---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
redirect_from:
  - /publications.html
---

My research publications are listed below. [ORCID record](https://orcid.org/0009-0008-5977-498X).

{% assign journals = site.publications | where: "category", "journals" | sort: "date" | reverse %}
{% assign conferences = site.publications | where: "category", "conferences" | sort: "date" | reverse %}

## Journal articles

{% for pub in journals %}
{% unless pub.published == false %}
{% include publication-item.html %}
{% endunless %}
{% endfor %}

## Conference papers

{% for pub in conferences %}
{% unless pub.published == false %}
{% include publication-item.html %}
{% endunless %}
{% endfor %}
