from django.db import models
from tinymce.models import HTMLField
from django.template.defaultfilters import default, slugify
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Blog(models.Model):
    title = models.CharField(max_length=300)
    featured_image = models.ImageField(upload_to='featured_images/', default='blog_post.jpg')
    slug = models.SlugField(editable=False, max_length=350)
    summary = models.TextField()
    content = models.TextField()
    tags = TaggableManager()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['date_posted']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug,
                                              'pk': self.pk})

