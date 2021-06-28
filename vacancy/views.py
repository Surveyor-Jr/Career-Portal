from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from .models import VacancyTypes, Vacancy
from blog.models import Blog

class HomePage(TemplateView):
    template_name = 'general_views/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['vacancy_type'] = VacancyTypes.objects.all()
        context['vacancy'] = Vacancy.objects.all().order_by('-date_posted')[:10]
        context['article'] = Blog.objects.order_by('-date_posted')[:2]
        return context

class Job(ListView):
    model = Vacancy
    template_name = 'vacancy/job_list.html'
    context_object_name = 'job'
    ordering = ['-date_posted']
    paginate_by = 20

class JobDetail(DetailView):
    model = Vacancy
    template_name = 'vacancy/job_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['other_jobs'] = Vacancy.objects.all().order_by('-date_posted')[:4]
        return context

class SearchResults(ListView):
    model = Vacancy
    template_name = 'vacancy/job_search_results.html'
    paginate_by = 40
    ordering = 'position'

    def get_queryset(self):
        query = self.request.GET.get('find')
        object_list = Vacancy.objects.filter(Q(position__icontains=query) | Q(qualifications__icontains=query))
        return object_list

class Category(ListView):
    model = Vacancy
    template_name = 'vacancy/job_category_list.html'
    context_object_name = 'job'
    paginate_by = 40

    def get_queryset(self):
        category = get_object_or_404(VacancyTypes, name=self.kwargs.get('name'))
        return Vacancy.objects.filter(vacancyType=category)

