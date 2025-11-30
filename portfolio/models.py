from django.db import models
from django.utils.text import slugify


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Font Awesome icon class or emoji')

    class Meta:
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.name


class Person(models.Model):
    """Represents a portfolio owner (can be multiple people)"""
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='team/', null=True, blank=True, help_text='Upload a profile photo')
    bio = models.TextField(blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    email_primary = models.EmailField(blank=True)
    email_secondary = models.EmailField(blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    github = models.URLField(blank=True, help_text='GitHub profile URL')
    linkedin = models.URLField(blank=True, help_text='LinkedIn profile URL')
    twitter = models.URLField(blank=True, help_text='Twitter profile URL')
    skills = models.ManyToManyField(Skill, blank=True, help_text='Select skills for this person')
    order = models.IntegerField(default=0, help_text='Display order (lower numbers first)')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'People'
        ordering = ['order']
    
    def __str__(self):
        return self.name


# Keep PortfolioInfo for backward compatibility (alias for migration purposes)
PortfolioInfo = Person


class Experience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='experiences', null=True, blank=True)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text='Leave blank if currently working here')
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='education', null=True, blank=True)
    school = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    graduation_year = models.IntegerField()

    class Meta:
        ordering = ['-graduation_year']
        verbose_name_plural = 'Education'

    def __str__(self):
        return f"{self.program} from {self.school}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True, help_text='Client title or company')
    quote = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, f'{i} stars') for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Testimonial from {self.client_name}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    category = models.CharField(max_length=100, blank=True, help_text='e.g., Web, Mobile, Design')
    technologies = models.ManyToManyField(Technology, blank=True, help_text='Select technologies used')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

