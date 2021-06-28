from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):
    list_display = ['title', 'author', 'summary', 'active']
    list_filter = ['active']
    search_fields = ['title', 'summary', 'author']
    actions = ['approve_post']
    summernote_fields = ['content']

    def approve_post(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Blog, BlogAdmin)
