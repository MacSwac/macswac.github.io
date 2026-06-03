---
title: 36 Famous Views of Tokyo
layout: default
permalink: /MyPrints/05Tokyo36views/
image: /assets/images/05Tokyo36views/Ikkei1.jpg
description: An alternative 36 views of Tokyo series
complete: "2/36(?)"
printingdate: 1871
series: 05_Tokyo36viewsalt
---

# 36 Famous Views of Tokyo
This seems to be either a standalone 36 views of Tokyo series, or possibly just two prints as new alternatives for Nr.1 and Nr.2 from the other 36 views of Tokyo series.
<table style="width:100%; border-collapse:collapse;">

{% assign prints = site.Ikkei | where: "series", "05_Tokyo36viewsalt" %}

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
<p> {{ post.en_title }}</p>

</td>
<td style="width:180px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

<p> {{ post.notes }}</p>

<p><strong>Source:</strong> {{ post.source }}</p>
</td>
</tr>

{% endfor %}

</table>
