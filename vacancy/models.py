from django.db import models
from django.utils import timezone
from django.template.defaultfilters import default, slugify
from django.urls import reverse
from django_countries.fields import CountryField
from PIL import Image
from tinymce.models import HTMLField
from datetime import date

class VacancyTypes(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Vacancy Type'

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    position = models.CharField(max_length=200)
    vacancyType = models.ForeignKey(VacancyTypes, on_delete=models.CASCADE)
    organization = models.CharField(max_length=200)
    country = CountryField()
    company_logo = models.ImageField(upload_to='logos/', default='vacancy.jpg')
    salary = models.CharField(max_length=300, null=True, blank=True)
    date_posted = models.DateField(default=timezone.now())
    closing_date = models.DateField()
    description = HTMLField()
    qualifications = HTMLField()
    source_link = models.URLField(null=True, blank=True)
    email = models.EmailField()
    slug = models.SlugField(max_length=500, editable=False) # TODO: Place Editable = False
    expired = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.position

    def save(self, *args, **kwargs):
        value = self.position
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug,
                                             'pk': self.pk})





