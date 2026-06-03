---
title: Famous views of Toyko
layout: default
permalink: /MyPrints/04TokyoMeisho/
image: /assets/images/04TokyoMeisho/Ikkei_亀井戸天満宮.jpg
description: Collections of unsorted Tokyo Meisho prints.
complete: "No"
printingdate: unknown
series: 04_TokyoMeisho
---

# Famous views of Tokyo

This is a collection of miscellaneous Tokyo Meisho (Famous places of Tokyo) prints. These appear to be quite rare, and by the fact that there are at least 2 different titles (Tokyo Meisho (東京名所) and Tokyo Meisho no Uchi (東京名所之内), seem to come from mutliple series. If a lot more are found, I might sort them in more detail. It is, as of now, to me, unclear if these constitute full series or abandoned projects.

<table style="width:100%; border-collapse:collapse;">

{% assign prints = site.Ikkei | where: "series", "04_TokyoMeisho" %}

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
