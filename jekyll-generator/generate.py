import csv
import re
from pathlib import Path

outdir = Path("_prints")
outdir.mkdir(exist_ok=True)

def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text

with open("prints.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader, start=1):

        filename = f"{i:03d}-{slugify(row['title'])}.md"

        image = f"/assets/images/0136views/Ikkei{i}.jpg"

        content = f"""---
title: {i:02d}-{row['title']}
en_title: {row['en_title']}
layout: post
series: 01_36viewsTokyo
image: {image}
description: 
source: Tokyo Metropolitan Library
---

{{% if page.image %}}
<img src="{{{{ page.image | relative_url }}}}">
{{% endif %}}
"""

        with open(outdir / filename, "w", encoding="utf-8") as out:
            out.write(content)

print("Done.")
