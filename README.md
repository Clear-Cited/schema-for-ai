# schema-for-ai

[![PyPI](https://img.shields.io/pypi/v/schema-for-ai.svg)](https://pypi.org/project/schema-for-ai/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21757576.svg)](https://doi.org/10.5281/zenodo.21757576)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Copy-paste **JSON-LD** templates tuned for how AI assistants extract and cite
information. Structured data helps ChatGPT, Perplexity, Gemini, and Google AI
resolve *what your product is* and pull clean facts into answers — instead of
guessing from raw HTML.

- Ready-to-edit templates for the schema types that matter most for AEO.
- A tiny **`validate.py`** (stdlib only) to sanity-check your JSON-LD.
- Notes on *why* each one helps AI extraction.

Drop a template in a `<script type="application/ld+json">…</script>` tag in your
page `<head>`, replace the `{{placeholders}}`, and validate.

## Why structured data helps AI answers

LLM answers lean heavily on **entities** (is "Acme" a company? a product? which
one?) and on **extractable facts** (price, category, FAQ answers). JSON-LD states
those explicitly and unambiguously, which makes you easier to identify, trust, and
quote. Pair it with a clean `llms.txt` (see our
[llms-txt-generator](https://github.com/Clear-Cited/llms-txt-generator)).

## Install

```bash
pip install schema-for-ai
```

That installs a `schema-for-ai` command that runs the validator. Cloning the repo
and running `python validate.py` does the same thing. Python 3.9+, no dependencies.

The templates below are copy-paste — they need no install at all. Each one also
ships as a file under [`templates/`](templates/), ready to validate:

```bash
schema-for-ai templates/organization.example.jsonld
```

## Validate

```bash
python validate.py mypage.jsonld
```

Checks valid JSON, the presence of `@context`/`@type`, and warns about missing
recommended fields for common types.

---

## Templates

### Organization
Establishes the entity. Put it on your homepage.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{{Company Name}}",
  "url": "https://{{domain}}",
  "logo": "https://{{domain}}/logo.png",
  "description": "{{One sentence on what you do and for whom}}",
  "sameAs": [
    "https://www.linkedin.com/company/{{handle}}",
    "https://x.com/{{handle}}",
    "https://www.crunchbase.com/organization/{{handle}}"
  ]
}
```

### SoftwareApplication / Product
For a tool or product page — gives AI the category, price, and ratings.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "{{Product Name}}",
  "applicationCategory": "{{e.g. DeveloperApplication}}",
  "operatingSystem": "{{e.g. Web, macOS, Linux}}",
  "description": "{{What it does, for whom, key differentiator}}",
  "offers": {
    "@type": "Offer",
    "price": "{{0.00}}",
    "priceCurrency": "{{USD}}"
  }
}
```

### FAQPage
AI loves FAQs — short Q/A pairs are highly extractable. Mark up real questions
buyers ask.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{A real question a buyer asks}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{A clear, self-contained answer in 1–3 sentences}}"
      }
    }
  ]
}
```

### Article / BlogPosting
For blog posts — author, date, and headline help AI attribute and cite you.

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{{Post title}}",
  "datePublished": "{{2026-01-01}}",
  "author": { "@type": "Person", "name": "{{Author}}" },
  "publisher": { "@type": "Organization", "name": "{{Company Name}}" },
  "description": "{{One-line summary}}"
}
```

### BreadcrumbList
Helps AI understand your site structure and the page's place in it.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://{{domain}}/" },
    { "@type": "ListItem", "position": 2, "name": "{{Section}}", "item": "https://{{domain}}/{{section}}/" }
  ]
}
```

## Tips

- One entity per page; keep `name`/`description` consistent everywhere (consistency
  is an entity signal).
- Put real, useful FAQ answers — don't keyword-stuff. AI (and Google) penalize it.
- Validate before shipping; a broken JSON-LD block is ignored entirely.

## Cite this

Every release is archived on Zenodo with a DOI, and the repo carries a
`CITATION.cff` so GitHub’s **Cite this repository** box works.

| | DOI |
|---|---|
| **Cite the software** (always resolves to the latest version) | [10.5281/zenodo.21757576](https://doi.org/10.5281/zenodo.21757576) |
| **Cite this exact release** (v0.1.0) | [10.5281/zenodo.21757577](https://doi.org/10.5281/zenodo.21757577) |

## Mirror

Mirrored to Codeberg at <https://codeberg.org/clear-cited/schema-for-ai>, tags
included, so the project does not depend on any single host.

## License

MIT © Clear Cited

---

Built by **[Clear Cited](https://clearcited.com)** — AEO/GEO for B2B SaaS &
developer tools. [See if AI recommends your product →](https://clearcited.com/free-teardown/)
