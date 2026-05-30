---
title: "36 views of Tokyo"
layout: post
permalink: /Ikkei/0136views
image: "/assets/images/DefaultIkkei.jpg"
description: "A small chuban version"
printingdate: "18700"
complete: "No"
---
---

# The 36 views of Tokyo

<table style="width:100%; border-collapse:collapse;">

{% for post in site.Ikkei.0136views %}

<tr>

<td style="width:300px; vertical-align:top; padding-bottom:30px;">

<img src="{{ post.image | relative_url }}"
     style="width:100%; max-width:240px; border-radius:8px;">
</td>

<td style="width:140px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

{{ post.printingdate }}
</td>

<td style="width:300px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

<h2 style="margin-top:0;">
<a href="{{ post.url | relative_url }}">
{{ post.title }}
</a>
</h2>

<p>{{ post.description }}</p>

</td>

<td style="width:140px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

{{ post.complete }}

</td>

</tr>

{% endfor %}

</table>



<table style="width:100%; border-collapse:collapse;">

{% for post in site.0136views %}

<tr>

<td style="width:300px; vertical-align:top; padding-bottom:30px;">

<img src="{{ post.image | relative_url }}"
     style="width:100%; max-width:240px; border-radius:8px;">
</td>

<td style="width:140px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

{{ post.printingdate }}
</td>

<td style="width:300px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

<h2 style="margin-top:0;">
<a href="{{ post.url | relative_url }}">
{{ post.title }}
</a>
</h2>

<p>{{ post.description }}</p>

</td>

<td style="width:140px; vertical-align:top; padding-left:20px; padding-bottom:30px;">

{{ post.complete }}

</td>

</tr>

{% endfor %}

</table>
