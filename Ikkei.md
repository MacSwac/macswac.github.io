---
title: "Ikkei"
layout: default
permalink: /Ikkei/
---

# Recipes

{% for post in site.Ikkei %}
  <div>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </div>
{% endfor %}
