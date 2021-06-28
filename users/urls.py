from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import Profile

urlpatterns = [
    path('auth/register/', user_views.register, name='register'),
    path('auth/login/', auth_views.LoginView.as_view(
        template_name='auth/login.html'),
         name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(
        template_name='general_views/home.html'),
         name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile/edit', user_views.profileEdit, name='profile-edit'),
    path('auth/password-reset', auth_views.PasswordResetView.as_view(
        template_name='auth/password_reset.html'),
         name='password-reset'),
    path('auth/password-reset/email-sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html'),
         name='password_reset_done'),
    path('auth/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('auth/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),
]