#!/usr/bin/env python
"""
Export Django portfolio to static HTML files for GitHub Pages
"""
import os
import shutil
from django.core.management import execute_from_command_line

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')

import django
django.setup()

from django.test import Client
from django.urls import reverse
from portfolio.models import Project

def export_to_static():
    """Export all pages to static HTML"""
    
    # Create docs directory for GitHub Pages
    docs_dir = 'docs'
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir)
    
    # Copy static files
    static_src = 'static'
    static_dest = os.path.join(docs_dir, 'static')
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dest)
    
    # Copy media files
    media_src = 'media'
    media_dest = os.path.join(docs_dir, 'media')
    if os.path.exists(media_src):
        shutil.copytree(media_src, media_dest)
    
    client = Client()
    
    # Export gifthun page
    print("Exporting gifthun page...")
    response = client.get('/')
    with open(os.path.join(docs_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(response.content.decode('utf-8'))
    
    # Export portfolio page
    print("Exporting portfolio page...")
    response = client.get('/portfolio/')
    with open(os.path.join(docs_dir, 'portfolio.html'), 'w', encoding='utf-8') as f:
        f.write(response.content.decode('utf-8'))
    
    # Export project detail pages
    print("Exporting project pages...")
    projects = Project.objects.all()
    projects_dir = os.path.join(docs_dir, 'projects')
    os.makedirs(projects_dir, exist_ok=True)
    
    for project in projects:
        url = f'/project/{project.slug}/'
        response = client.get(url)
        filename = os.path.join(projects_dir, f'{project.slug}.html')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.content.decode('utf-8'))
        print(f"  - {project.title}")
    
    # Export contact page
    print("Exporting contact page...")
    response = client.get('/contact/')
    with open(os.path.join(docs_dir, 'contact.html'), 'w', encoding='utf-8') as f:
        f.write(response.content.decode('utf-8'))
    
    print(f"\n✅ Static site exported to '{docs_dir}/' directory")
    print("\nNext steps:")
    print("1. Commit the 'docs' folder to git")
    print("2. Push to GitHub")
    print("3. Go to Settings > Pages")
    print("4. Select 'Deploy from a branch' and choose 'main' branch, '/docs' folder")

if __name__ == '__main__':
    export_to_static()
