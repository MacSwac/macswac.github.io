---
title: "My Prints"
layout: default
---

<main>
  <header><h1>{{ include.title | default: page.title }}</h1></header>
  <nav class="smooth">
    {% for post in site.MyPrints %}
    <div><a href="{{ post.url | relative_url }}">{{ post.title }}</a></div>
    {% endfor %}
  </nav>
</main>
