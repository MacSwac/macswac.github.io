---
title: 48 views of Tokyo 
layout: default
permalink: /MyPrints/02_48views/
image: /assets/images/0248views/Ikkei1.jpg
description: A bigger series
complete: "No"
printingdate: unknown
series: 02_48viewsTokyo
---

# 48 views of Tokyo

Here is one of Ikkei's most celebrated series, 48 views of Tokyo. The numbering of these prints is not yet fully determined, as some of the prints in the main source for this, the Tokyo Metropolitan Library, have had their margins cut, so the number is missing. For some, it was however, possible to assign a number from other sources (Edo Tokyo, Harashobu). The known prints with unknown number are below the numbered ones here. There are some prints missing as these do not make up 48+title page. The title page has the prints in order but I haven't found the time to yet examine the kanjis and sort out the numbering. 

<table style="width:100%; border-collapse:collapse;">

{% assign prints = site.Ikkei | where: "series", "02_48viewsTokyo" %}

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
