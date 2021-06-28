from django.contrib import admin
from .models import VacancyTypes, Vacancy

class VacancyTypesAdmin(admin.ModelAdmin):
    pass

class VacancyAdmin(admin.ModelAdmin):
    list_display = ['date_posted', 'position', 'organization', 'email']
    list_filter = ['vacancyType', 'country']
    search_fields = ['position', 'qualifications']

admin.site.register(VacancyTypes, VacancyTypesAdmin)
admin.site.register(Vacancy, VacancyAdmin)
