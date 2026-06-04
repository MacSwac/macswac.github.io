---
title: Triptychs
layout: default
permalink: /MyPrints/15Triptychs/
image: /assets/images/15Triptychs/Ikkei_海運橋為換坐之図.jpg
description: Miscellaneous prints
complete: "No"
printingdate: unknown
series: 15Triptychs
---

# Triptychs

These are the Triptychs by Ikkei Shosai. 
<table style="width:100%; border-collapse:collapse;">

{% assign prints = site.Ikkei | where: "series", "15Triptychs" %}

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
<p><strong>Date:</strong> {{ post.printing_date }}</p>
</td>
</tr>

{% endfor %}

</table>
