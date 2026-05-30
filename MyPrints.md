---
title: "My Prints"
layout: default
permalink: /MyPrints/
---
{% assign countries = site.MyPrints | group_by: "country" %}

{% for country in countries %}
  <tr>
    <td>
      <a href="/MyPrints/{{ country.name | slugify }}/">
        {{ country.name }}
      </a>
    </td>
  </tr>
{% endfor %}
