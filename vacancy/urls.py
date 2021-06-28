from django.urls import path
from .views import Job, JobDetail, SearchResults, Category

urlpatterns = [
    path('', Job.as_view(), name='job-list'),
    path('job/<slug:slug>-<int:pk>/', JobDetail.as_view(), name='job-detail'),
    path('job/', SearchResults.as_view(), name='job-result'),
    path('job/category/<str:name>/', Category.as_view(), name='job-by-category'),
]