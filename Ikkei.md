---
title: Ikkei
layout: default
permalink: /Ikkei/
---

# The prints of Ikkei Shosai

<table style="width:100%; border-collapse:collapse;">

{% for series in site.series %}

<tr>

<td style="width:260px; vertical-align:top; padding-bottom:30px;">

<img src="{{ series.image | relative_url }}"
     style="width:100%; min-width:250px; max-width:500px; border-radius:8px;">

</td>

<td style="vertical-align:top; padding-left:20px; padding-bottom:30px;">

<h2>
<a href="{{ series.url | relative_url }}">
{{ series.title }}
</a>
</h2>

<p>{{ series.description }}</p>

</td>

<td style="width:180px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

<p><strong>Date:</strong> {{ series.printingdate }}</p>
</td>

<td style="width:180px; vertical-align:top; padding-left:20px; padding-bottom:30px;">


<p><strong>Complete:</strong> {{ series.complete }}</p>

</td>

</tr>

{% endfor %}

</table>
