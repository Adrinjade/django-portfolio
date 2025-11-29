from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from .models import Project, Skill, Person, Experience, Education, Testimonial
from .forms import ContactForm


def index(request):
    projects = Project.objects.all()
    people = Person.objects.all()  # Get all people
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    testimonials = Testimonial.objects.all()
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query)
        )
    
    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        projects = projects.filter(category=category_filter)
    
    # Get unique categories for filter dropdown
    categories = Project.objects.values_list('category', flat=True).distinct()
    
    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'people': people,  # Pass all people to template
        'skills': skills,
        'experiences': experiences,
        'education': education,
        'testimonials': testimonials,
        'search_query': search_query,
        'categories': categories,
        'selected_category': category_filter,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def contact(request):
    people = Person.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Contact form submission from {name}'
            body = f'From: {name} <{email}>\n\n{message}'
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)
            return redirect('portfolio:contact_thanks')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form, 'people': people})


def contact_thanks(request):
    return render(request, 'portfolio/contact_thanks.html')
