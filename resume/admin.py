from django.contrib import admin
from .models import (
    Personal,
    Contact,
    Skill,
    Experience,
    Language,
    Hobby,
    Education,
    Reference,
)


class PersonalAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    list_display = ['person', 'email', 'phone_number']
    search_fields = ['email', 'person']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating']
    search_fields = ['name']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'organization']
    search_fields = ['organization', 'position']


class LanguageAdmin(admin.ModelAdmin):
    pass


class HobbyAdmin(admin.ModelAdmin):
    pass


class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'qualification']
    search_fields = ['qualification']


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position', 'organization']
    search_fields = ['fullname', 'organization', 'position']


admin.site.register(Personal, PersonalAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Reference, ReferenceAdmin)