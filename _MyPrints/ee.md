---
title: "Pup"
layout: post
image: "/assets/images/DefaultIkkei.jpg"
description: "A small chuban version"
printingdate: "18700"
complete: "No"
country: "Iceland"
---



<table>

{% assign posts = site.MyPrints | where: "country", page.country %}

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
