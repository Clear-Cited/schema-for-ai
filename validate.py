#!/usr/bin/env python3
"""validate.py — sanity-check a JSON-LD file for AI/SEO structured data.

Checks: valid JSON, presence of @context and @type, and warns about missing
recommended fields for common schema.org types. Stdlib only.

Usage:
    python validate.py mypage.jsonld
    python validate.py *.json

Made by Clear Cited — https://clearcited.com
"""
from __future__ import annotations
import json, sys

RECOMMENDED = {
    "Organization": ["name", "url", "description", "sameAs"],
    "SoftwareApplication": ["name", "applicationCategory", "description"],
    "Product": ["name", "description", "offers"],
    "FAQPage": ["mainEntity"],
    "BlogPosting": ["headline", "datePublished", "author"],
    "Article": ["headline", "datePublished", "author"],
    "BreadcrumbList": ["itemListElement"],
}


def check(obj, path="root"):
    problems, warnings = [], []
    if not isinstance(obj, dict):
        problems.append("%s: top-level JSON-LD should be an object" % path)
        return problems, warnings
    if "@context" not in obj:
        problems.append("%s: missing @context (use \"https://schema.org\")" % path)
    t = obj.get("@type")
    if not t:
        problems.append("%s: missing @type" % path)
    else:
        for field in RECOMMENDED.get(t, []):
            if field not in obj:
                warnings.append("%s: %s is missing recommended field '%s'" % (path, t, field))
    return problems, warnings


def validate_file(fn):
    print("== %s ==" % fn)
    try:
        data = json.load(open(fn, encoding="utf-8"))
    except json.JSONDecodeError as e:
        print("  INVALID JSON: %s" % e)
        return False
    except OSError as e:
        print("  cannot read: %s" % e)
        return False

    items = data if isinstance(data, list) else [data]
    ok = True
    for i, obj in enumerate(items):
        p, w = check(obj, "item[%d]" % i if len(items) > 1 else obj.get("@type", "root"))
        for m in p:
            print("  ERROR:   " + m); ok = False
        for m in w:
            print("  warning: " + m)
    if ok:
        print("  valid JSON-LD" + (" (with warnings above)" if any(True for _ in []) else ""))
    return ok


def main():
    files = sys.argv[1:]
    if not files:
        sys.exit("usage: python validate.py file.jsonld [more...]")
    all_ok = True
    for fn in files:
        all_ok = validate_file(fn) and all_ok
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
