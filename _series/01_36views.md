---
title: 36 views of Tokyo 
layout: default
permalink: /MyPrints/01_36views/
image: /assets/images/DefaultIkkei.jpg
description: A small series
complete: "No"
printingdate: unknown
series: 01_36viewsTokyo
---

# 36 views of Tokyo

<table style="width:100%; border-collapse:collapse;">

{% assign prints = site.Ikkei | where: "series", "01_36viewsTokyo" %}

{% for post in prints %}

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


</td>
<td style="width:180px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

<p><strong>Date:</strong> {{ post.notes }}</p>

<p><strong>Date:</strong> {{ post.source }}</p>
</td>
</tr>

{% endfor %}

</table>
