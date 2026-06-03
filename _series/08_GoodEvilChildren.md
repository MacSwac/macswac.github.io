---
title: Good and Evil Houses/Lessons
layout: default
permalink: /Ikkei/08GoodEvil/
image: /assets/images/08GoodEvil/Ikkei11.jpg
description: 
complete: "No"
printingdate: unknown
series: 08GoodEvil
---

# Good and Evil Houses/Lessons

This seems to be a picturebook with at least 12 pages (2 prints per page). They have quite varied coloration, as can be seen by comparing entry 11 and 12. I purposely did not cut up the pictures to only include the correct pages, to keep the full images.ss
<table style="width:100%; border-collapse:collapse;">

{% assign prints = site.Ikkei | where: "series", "08GoodEvil" %}

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
