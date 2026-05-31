---
title: 36 comic views of Tokyo 
layout: default
permalink: /MyPrints/03_36comic/
image: /assets/images/0336comic/Ikkei1.jpg
description: A small series
complete: "No"
printingdate: unknown
series: 01_36comicTokyo
---

# 36 comic views of Tokyo
Since these prints are not numbered through, the ordering is somewhat arbitrary. I found one source online with all of the prints bound in an album that looks somewhat original and decided to use that ordering. However, there is no good evidence that that is the "correct" ordering if there ever was one. I have also not found a title page print.
<table style="width:100%; border-collapse:collapse;">

{% assign prints = site.Ikkei | where: "series", "01_36comicTokyo" %}

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
