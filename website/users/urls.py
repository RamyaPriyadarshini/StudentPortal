from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='Logout')
]
