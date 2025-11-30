from django.contrib import admin
from .models import Project, Skill, Person, Experience, Education, Testimonial, Technology


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    fields = ('school', 'program', 'graduation_year', 'description')


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1
    fields = ('title', 'company', 'start_date', 'end_date', 'is_current', 'description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'link', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('technologies',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'order')
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'photo', 'bio', 'contact_number', 'order')}),
        ('Emails', {'fields': ('email_primary', 'email_secondary')}),
        ('Social Media', {'fields': ('facebook', 'instagram', 'github', 'linkedin', 'twitter')}),
        ('Skills', {'fields': ('skills',)}),
    )
    inlines = [EducationInline, ExperienceInline]
    filter_horizontal = ('skills',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_current')
    list_filter = ('company', 'is_current', 'start_date')
    search_fields = ('title', 'company', 'description')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('program', 'school', 'graduation_year')
    list_filter = ('graduation_year', 'school')
    search_fields = ('program', 'school')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'role', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('client_name', 'quote')
