from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('article/<slug:slug>-<int:pk>/', PostDetail.as_view(), name='blog-detail'),
    path('article/<slug:slug>-<int:pk>/update/', PostUpdate.as_view(), name='blog-update'),
    path('article/<slug:slug>-<int:pk>/delete/', PostDelete.as_view(), name='blog-delete'),
    path('search/', PostSearch.as_view(), name='post-result'),
    path('new-article/', PostCreate.as_view(), name='new-article'),
]