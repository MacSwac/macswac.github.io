---
title: MyPrints
layout: default
permalink: /MyPrints/
---

# Travel

<table style="width:100%; border-collapse:collapse;">

{% for country in site.contry %}

<tr>

<td style="width:260px; vertical-align:top; padding-bottom:30px;">

<img src="{{ country.image | relative_url }}"
     style="width:100%; max-width:240px; border-radius:8px;">

</td>

<td style="vertical-align:top; padding-left:20px;">

<h2>
<a href="{{ country.url | relative_url }}">
{{ country.title }}
</a>
</h2>

<p>{{ country.description }}</p>

</td>

</tr>

{% endfor %}

</table>
