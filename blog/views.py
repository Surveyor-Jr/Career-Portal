from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Blog
from .forms import ArticleForm
from taggit.models import Tag

class PostList(ListView):
    model = Blog
    template_name = 'blog/post_list.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tags'] = Tag.objects.all()
        return context

class PostDetail(DetailView):
    model = Blog
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['other_articles'] = Blog.objects.order_by('date_posted')[:6]
        context['tags'] = Tag.objects.all()
        return context

class PostSearch(ListView):
    model = Blog
    template_name = 'blog/post_search_results.html'
    paginate_by = 30
    ordering = 'title'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['other_articles'] = Blog.objects.order_by('date_posted')[:6]
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get('find')
        object_list = Blog.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
        return object_list

class PostCreate(CreateView):
    template_name = 'blog/create_article.html'
    form_class = ArticleForm
    success_message = "Your article has been added to the blog and is now pending verification. It might take" \
                      "at-least 24-hours until your article is public."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['other_articles'] = Blog.objects.order_by('date_posted')[:6]
        context['tags'] = Tag.objects.all()
        return context

class PostUpdate(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/create_article.html'
    form_class = ArticleForm
    success_message = "Your post has been updated"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['other_articles'] = Blog.objects.order_by('date_posted')[:6]
        context['tags'] = Tag.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDelete(UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog/post_delete_confirmation.html'
    success_url = 'post-list'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False