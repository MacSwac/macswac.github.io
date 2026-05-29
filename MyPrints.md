---
title: "My Prints"
layout: default
permalink: /MyPrints/
---

# Travel

{% for post in site.MyPrints %}
  <div>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </div>
{% endfor %}
