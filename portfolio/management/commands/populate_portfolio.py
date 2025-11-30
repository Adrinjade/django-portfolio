from django.core.management.base import BaseCommand
from portfolio.models import Skill, Person


class Command(BaseCommand):
    help = 'Populate portfolio people and skills'

    def handle(self, *args, **options):
        # Create or update Aldrin's profile
        aldrin, created = Person.objects.get_or_create(
            pk=1,
            defaults={
                'name': 'Welcome',
                'contact_number': '09193213033',
                'email_primary': 'Aldrinjadesaura11@gmail.com',
                'email_secondary': 'aldrinjade.s11@yahoo.com',
                'facebook': 'Aljin Gc',
                'instagram': 'Aldrin jade saura',
                'bio': 'Creative developer passionate about building web and game projects',
                'order': 0,
            }
        )
        if not created:
            aldrin.name = 'Welcome'
            aldrin.contact_number = '09193213033'
            aldrin.email_primary = 'Aldrinjadesaura11@gmail.com'
            aldrin.email_secondary = 'aldrinjade.s11@yahoo.com'
            aldrin.facebook = 'Aljin Gc'
            aldrin.instagram = 'Aldrin jade saura'
            aldrin.bio = 'Creative developer passionate about building web and game projects'
            aldrin.order = 0
            aldrin.save()
        
        # Create or update Neil's profile
        neil, created = Person.objects.get_or_create(
            pk=2,
            defaults={
                'name': 'Neil Christian G. Carpio',
                'contact_number': '09087034486',
                'facebook': 'Neil Christian Carpio',
                'bio': 'Software developer passionate about creating innovative solutions',
                'order': 1,
            }
        )
        if not created:
            neil.name = 'Neil Christian G. Carpio'
            neil.contact_number = '09087034486'
            neil.facebook = 'Neil Christian Carpio'
            neil.bio = 'Software developer passionate about creating innovative solutions'
            neil.order = 1
            neil.save()
        
        # Create all skills
        aldrin_skills = ['Python', 'Java', 'PHP', 'Blender', 'C#']
        neil_skills = ['Java', 'Python', 'C++', 'C#']
        all_skills = set(aldrin_skills + neil_skills)
        
        skill_objects = {}
        for skill_name in all_skills:
            skill, _ = Skill.objects.get_or_create(name=skill_name)
            skill_objects[skill_name] = skill
        
        # Assign skills to Aldrin
        aldrin.skills.set([skill_objects[skill] for skill in aldrin_skills])
        
        # Assign skills to Neil
        neil.skills.set([skill_objects[skill] for skill in neil_skills])
        
        self.stdout.write(self.style.SUCCESS('Portfolio people and skills populated successfully!'))

