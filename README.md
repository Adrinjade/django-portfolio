# django-portfolio

A modern, feature-rich Django portfolio website showcasing your projects, experience, education, and skills.

## Features

✨ **Core Features**
- **About Section**: Display your name, contact info, and skills
- **Projects**: Showcase your work with descriptions, links, images, and categories
- **Experience Timeline**: Highlight your professional work history
- **Education**: List your degrees and certifications
- **Testimonials**: Display client feedback and reviews
- **Contact Form**: Collect inquiries from visitors
- **Search & Filter**: Find projects by keyword or category

🎨 **Design**
- Modern, responsive layout (mobile, tablet, desktop)
- Beautiful color scheme with smooth animations
- Dark mode-friendly with gradient accents
- Optimized typography and spacing

## Quick Start

### 1. Clone and setup

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Initialize the database

```bash
python manage.py migrate
python manage.py populate_portfolio  # Populates your info & skills
```

### 3. Create an admin account

```bash
python manage.py createsuperuser
```

### 4. Run the server

```bash
python manage.py runserver
```

Visit:
- **Site**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## Adding Content

### Projects
Go to `/admin/` → Projects → Add Project
- Title, description, link, category, and optional image

### Experience
Go to `/admin/` → Experience → Add Experience
- Job title, company, dates, and description
- Mark as "Current" if you're still working there

### Education
Go to `/admin/` → Education → Add Education
- School, program, graduation year, and optional notes

### Testimonials
Go to `/admin/` → Testimonials → Add Testimonial
- Client name, role, quote, and star rating (1-5)

### Skills
Go to `/admin/` → Skills → Add Skill
- Already pre-populated with: Python, Java, PHP, Blender, C#

## Customization

### Update Your Info
Edit `/admin/` → Portfolio Info:
- Change name and contact number

### Change Colors
Edit `static/css/styles.css` and modify the `:root` variables:
```css
:root {
  --primary: #0f1724;
  --accent: #00d4ff;
  /* ... */
}
```

### Add Logo or Profile Picture
Create a `ProfilePicture` model or upload a static image to `static/images/` and reference it in templates.

## Project Structure

```
django-portfolio/
├── portfolio/              # Main app
│   ├── models.py          # Data models
│   ├── views.py           # View logic
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin customization
│   └── migrations/        # Database migrations
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   └── portfolio/         # App templates
├── static/css/            # Stylesheets
├── media/                 # User uploads (project images)
├── db.sqlite3             # Development database
├── manage.py              # Django CLI
├── requirements.txt       # Dependencies
└── portfolio_site/        # Project settings
```

## Dependencies

- **Django 4.2+**: Web framework
- **Pillow 10.0+**: Image processing for project thumbnails

## Deployment

For production deployment:
1. Set `DEBUG = False` in `settings.py`
2. Use a production database (PostgreSQL recommended)
3. Configure static/media file serving with nginx or S3
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Set `SECRET_KEY` via environment variable
6. Configure `ALLOWED_HOSTS`

Example for Gunicorn:
```bash
pip install gunicorn
gunicorn portfolio_site.wsgi:application
```

## License

MIT

## Support

For issues or questions, check the admin panel at `/admin/` to manage all content.
