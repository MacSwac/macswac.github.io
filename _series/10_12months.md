---
title: 12 Months
layout: default
permalink: /Ikkei/10TwelveMonths/
image: /assets/images/10TwelveMonths/Ikkei11.jpg
description: A small series with 12 (?) famous spots in Tokyo represented by one of the months/
complete: "1/12(?)"
printingdate: unknown
series: 10_TwelveMonths
---

# 12 Months

<table style="width:100%; border-collapse:collapse;">

{% assign prints = site.Ikkei | where: "series", "10_TwelveMonths" %}

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
e
