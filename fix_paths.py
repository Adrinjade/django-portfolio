#!/usr/bin/env python3
"""Fix absolute paths to relative paths in docs/ HTML files for GitHub Pages."""
import os
import re

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace absolute paths with relative
    replacements = [
        (r'href="/static/', 'href="./static/'),
        (r'src="/static/', 'src="./static/'),
        (r'href="/media/', 'href="./media/'),
        (r'src="/media/', 'src="./media/'),
        (r'href="/"(?![^>]*>)', 'href="./"'),
        (r'href="/contact/"', 'href="./contact.html"'),
        (r'src="/static/js/main.js"', 'src="./static/js/main.js"'),
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    # Also replace root links like <a href="/">Home</a> but not inside already changed paths
    # Be careful to only replace nav/footer links, not ones in dynamic content
    content = re.sub(r'<a href="/">', '<a href="./">', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Fixed: {filepath}')

# Process all HTML files in docs/
for root, dirs, files in os.walk('docs'):
    for f in files:
        if f.endswith('.html'):
            fix_html_file(os.path.join(root, f))

print('\nAll paths fixed!')
