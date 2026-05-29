title: "Travel"
layout: default
permalink: /MyPrints/
---

# Travel

<table style="width:100%; border-collapse:collapse;">

{% for post in site.travel %}

<tr>

<td style="width:260px; vertical-align:top; padding-bottom:30px;">

<img src="{{ post.image | relative_url }}"
     style="width:100%; max-width:240px; border-radius:8px;">

</td>

<td style="vertical-align:top; padding-left:20px; padding-bottom:30px;">

<h2 style="margin-top:0;">
<a href="{{ post.url | relative_url }}">
{{ post.title }}
</a>
</h2>

</td>

</tr>

{% endfor %}

</table>
