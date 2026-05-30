---
layout: default
title: Japan
country: Iceland
---

<table>

{% assign posts = site.Myprints | where: "country", page.country %}

{% for post in posts %}

<tr>
  <td>
    <img src="{{ post.image | relative_url }}" width="200">
  </td>

  <td>
    <a href="{{ post.url | relative_url }}">
      {{ post.title }}
    </a>
  </td>

  <td>
    {{ post.description }}
  </td>
</tr>

{% endfor %}

</table>
