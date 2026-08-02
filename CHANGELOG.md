# Changelog

All notable changes to this project are documented here.
This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html), and
the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Every release is archived on Zenodo. The **concept DOI**
[10.5281/zenodo.21757576](https://doi.org/10.5281/zenodo.21757576) always resolves to the latest
version; each release below also has its own version DOI.

## [0.1.0] - 2026-08-02

First public release.

### Added

- `validate.py` — a dependency-free JSON-LD checker that verifies valid JSON,
  the presence of `@context` and `@type`, and warns about missing recommended
  fields for Organization, Product, SoftwareApplication, FAQPage, Article,
  BlogPosting and BreadcrumbList.
- Copy-paste templates in the README, and matching files under `templates/`.
- `CITATION.cff` and `.zenodo.json`, so the repository is citable and archives
  automatically on release.

### Notes

- Version DOI: [10.5281/zenodo.21757577](https://doi.org/10.5281/zenodo.21757577)
- Published to PyPI as [`schema-for-ai`](https://pypi.org/project/schema-for-ai/) via Trusted Publishing, with provenance attestations.
- Mirrored to [Codeberg](https://codeberg.org/clear-cited/schema-for-ai), tags included.

[0.1.0]: https://github.com/Clear-Cited/schema-for-ai/releases/tag/v0.1.0
