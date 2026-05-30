---
title: Iceland
layout: default
permalink: /MyPrints/iceland/
image: /assets/images/DefaultIkkei.jpg
description: Volcanoes, glaciers, waterfalls and long road trips.
---

# Iceland

<table style="width:100%; border-collapse:collapse;">

{% assign trips = site.MyPrints | where: "country", "Iceland" %}

{% for post in trips %}

<tr>

<td style="width:260px; vertical-align:top; padding-bottom:30px;">

<img src="{{ post.image | relative_url }}"
     style="width:100%; max-width:240px; border-radius:8px;">

</td>

<td style="vertical-align:top; padding-left:20px;">

<h2>
<a href="{{ post.url | relative_url }}">
{{ post.title }}
</a>
</h2>

<p>{{ post.description }}</p>

</td>

</tr>

{% endfor %}

</table>
