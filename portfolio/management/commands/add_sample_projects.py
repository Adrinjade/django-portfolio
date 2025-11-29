from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Add sample game and web projects to portfolio'

    def handle(self, *args, **options):
        # Sample Web Projects
        web_projects = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce platform built with Django and React. Includes user authentication, product catalog, shopping cart, and secure payment integration. Features real-time inventory management and admin dashboard for order tracking.',
                'category': 'Web',
                'link': 'https://github.com/yourusername/ecommerce-platform',
            },
            {
                'title': 'Social Media Dashboard',
                'description': 'A responsive web application for managing multiple social media accounts. Built with Django REST Framework and React.js. Allows scheduling posts, analytics tracking, and engagement monitoring across platforms.',
                'category': 'Web',
                'link': 'https://github.com/yourusername/social-media-dashboard',
            },
            {
                'title': 'Project Management Tool',
                'description': 'A collaborative project management application with real-time updates using WebSockets. Features task boards, team collaboration, file sharing, and progress tracking. Built with Django and Vue.js.',
                'category': 'Web',
                'link': 'https://github.com/yourusername/project-management-tool',
            },
            {
                'title': 'Blog Platform',
                'description': 'A modern blogging platform with markdown support, SEO optimization, and social sharing. Includes user authentication, comment system, and advanced search functionality. Built with Django and TailwindCSS.',
                'category': 'Web',
                'link': 'https://github.com/yourusername/blog-platform',
            },
            {
                'title': 'Task Management API',
                'description': 'RESTful API for task and todo management with JWT authentication. Supports multiple workspaces, team collaboration, and real-time notifications. Fully documented with Swagger/OpenAPI.',
                'category': 'Web',
                'link': 'https://github.com/yourusername/task-api',
            },
        ]

        # Sample Game Projects
        game_projects = [
            {
                'title': '2D Platformer Game',
                'description': 'A challenging 2D platformer game developed with Unity and C#. Features 15+ levels with increasing difficulty, physics-based gameplay, collectibles, and boss battles. Includes particle effects and smooth animations.',
                'category': 'Game',
                'link': 'https://itch.io/yourusername/platformer-game',
            },
            {
                'title': 'Puzzle Game',
                'description': 'An addictive puzzle game with 100+ levels featuring different mechanics. Built with Godot Engine. Includes leaderboards, achievements, and difficulty progression. Optimized for mobile and desktop.',
                'category': 'Game',
                'link': 'https://itch.io/yourusername/puzzle-game',
            },
            {
                'title': 'Space Shooter',
                'description': 'An arcade-style space shooter game made with C# and Unity. Fight waves of enemies with upgradeable weapons, power-ups, and boss encounters. Features high-quality sound effects and visual effects.',
                'category': 'Game',
                'link': 'https://itch.io/yourusername/space-shooter',
            },
            {
                'title': 'Adventure Game',
                'description': 'A story-driven adventure game built with Godot Engine. Features an engaging narrative, exploration, puzzle-solving, and character interactions. High-quality pixel art and atmospheric soundtrack.',
                'category': 'Game',
                'link': 'https://itch.io/yourusername/adventure-game',
            },
            {
                'title': 'Multiplayer RPG',
                'description': 'A multiplayer RPG with real-time combat system developed with Unity and Photon networking. Features character progression, quests, dungeons, and PvP battles. Supports cross-platform play.',
                'category': 'Game',
                'link': 'https://yourgame.com/multiplayer-rpg',
            },
        ]

        # Add all projects
        all_projects = web_projects + game_projects
        created_count = 0

        for project_data in all_projects:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'description': project_data['description'],
                    'category': project_data['category'],
                    'link': project_data['link'],
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created: {project.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⊘ Already exists: {project.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Successfully added {created_count} new sample projects!'
            )
        )
