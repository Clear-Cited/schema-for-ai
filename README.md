# schema-for-ai

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

## License

MIT © Clear Cited

---

Built by **[Clear Cited](https://clearcited.com)** — AEO/GEO for B2B SaaS &
developer tools. [See if AI recommends your product →](https://clearcited.com/free-teardown/)
