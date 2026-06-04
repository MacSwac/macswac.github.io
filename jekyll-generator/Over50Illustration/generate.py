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

# ==========================
# Known-number prints
# ==========================

with open("prints.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader, start=1):

        title = row.get("title", "").strip()

        # Skip missing print numbers
        if not title:
            continue

        filename = f"{i:03d}-{slugify(title)}.md"

        image = f"/assets/images/09_画解五十余箇條/Ikkei{i}.jpg"

        content = f"""---
title: \"{i:03d}-{title}\" 
en_title: \"{row['en_title']}\" 
layout: post
series: 09_画解五十余箇條
image: {image}
description: \"{row['description']}\" 
source: \"{row['source']}\" 
---

{{% if page.image %}}
<img src="{{{{ page.image | relative_url }}}}">
{{% endif %}}
"""

        with open(outdir / filename, "w", encoding="utf-8") as out:
            out.write(content)

# ==========================
# Unknown-number prints
# ==========================

unknown_number = 900

with open("prints_unknown.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        title = row.get("title", "").strip()

        if not title:
            continue

        slug = slugify(title)

        filename = f"{unknown_number:03d}-{slug}.md"

        image = f"/assets/images/09_画解五十余箇條/Ikkei_{slug}{row['tag']}.jpg"

        content = f"""---
title: \"{row['numbers']}: {title}\" 
en_title: \"{row['en_title']}\" 
layout: post
series: 09_画解五十余箇條
image: {image}
description: \"{row['description']}\" 
source: \"{row['source']}\" 
---

{{% if page.image %}}
<img src="{{{{ page.image | relative_url }}}}">
{{% endif %}}
"""

        with open(outdir / filename, "w", encoding="utf-8") as out:
            out.write(content)

        unknown_number += 1

print("Done.")
