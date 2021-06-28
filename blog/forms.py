from django import forms
from .models import Blog
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class ArticleForm(forms.ModelForm):
    content = SummernoteTextFormField()

    class Meta:
        model = Blog
        fields = ['title', 'featured_image', 'summary', 'content', 'tags']