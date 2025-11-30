#!/usr/bin/env python3
"""
Simple accessibility scanner for exported `docs/` HTML files.
Uses regex heuristics (no external dependencies).
Checks:
 - presence of <html lang="...">
 - images missing alt or empty alt
 - form inputs with id but no matching <label for="id">
 - multiple H1s and heading order issues
 - links with no text and no aria-label/title

Usage: python tools/a11y_scan.py docs/
"""
import sys
import os
import re


def scan_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    issues = []

    # lang attribute
    if not re.search(r'<html[^>]*\blang\s*=\s*"[a-zA-Z-]+"', html, re.IGNORECASE):
        issues.append('Missing <html lang="...">')

    # images
    for m in re.finditer(r'<img[^>]*>', html, re.IGNORECASE):
        tag = m.group(0)
        src_match = re.search(r'src\s*=\s*"([^"]+)"', tag)
        alt_match = re.search(r'alt\s*=\s*"([^"]*)"', tag)
        src = src_match.group(1) if src_match else '(unknown)'
        if not alt_match:
            issues.append(f'Image without alt: {src}')
        elif alt_match.group(1).strip() == '':
            issues.append(f'Image with empty alt (decorative): {src}')

    # forms: look for inputs without label by simple heuristics
    for m in re.finditer(r'<(input|textarea|select)([^>]*)>', html, re.IGNORECASE):
        tag = m.group(0)
        attrs = m.group(2)
        if re.search(r'type\s*=\s*"(hidden|submit|button)"', attrs, re.IGNORECASE):
            continue
        idm = re.search(r'id\s*=\s*"([^"]+)"', attrs, re.IGNORECASE)
        if idm:
            iid = idm.group(1)
            if not re.search(r'<label[^>]*for\s*=\s*"' + re.escape(iid) + '"', html, re.IGNORECASE):
                issues.append(f'Input may be missing label for id "{iid}": {tag[:60]}')

    # headings: count h1 and check order by simple scan
    htags = re.findall(r'<h([1-6])[^>]*>', html, re.IGNORECASE)
    h1_count = sum(1 for h in htags if h == '1')
    if h1_count > 1:
        issues.append(f'Multiple H1 elements ({h1_count})')
    last = 0
    for level in (int(x) for x in htags):
        if level - last > 1:
            issues.append('Heading order jumps detected (e.g., h2 -> h4)')
            break
        last = level

    # links with no text
    for m in re.finditer(r'<a[^>]*>(.*?)</a>', html, re.IGNORECASE | re.DOTALL):
        txt = re.sub(r'<[^>]+>', '', m.group(1) or '').strip()
        tag = m.group(0)
        if txt == '' and not re.search(r'aria-label\s*=\s*"', tag) and not re.search(r'title\s*=\s*"', tag):
            issues.append(f'Link with no text and no label/title: {tag[:60]}')

    return issues


def scan_folder(folder):
    results = {}
    for root, _, files in os.walk(folder):
        for f in files:
            if f.lower().endswith('.html'):
                path = os.path.join(root, f)
                issues = scan_file(path)
                if issues:
                    results[path] = issues
    return results


def main():
    if len(sys.argv) < 2:
        print('Usage: python tools/a11y_scan.py <docs-folder>')
        sys.exit(1)
    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print('Not a folder:', folder)
        sys.exit(1)
    res = scan_folder(folder)
    if not res:
        print('No basic accessibility issues found.')
        sys.exit(0)
    print('\nAccessibility scan results:')
    for path, issues in res.items():
        print('\n--', path)
        for issue in issues:
            print('   -', issue)
    sys.exit(2)


if __name__ == '__main__':
    main()
