---
title: "My Prints"
layout: default
permalink: /Ikkei/
---
{% assign countries = site.MyPrints | group_by: "country" %}

{% for country in countries %}
  <tr>
    <td>
      <a href="/travel/{{ country.name | slugify }}/">
        {{ country.name }}
      </a>
    </td>
  </tr>
{% endfor %}
