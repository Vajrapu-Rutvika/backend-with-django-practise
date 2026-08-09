from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/',views.post_detail, name='post_detail'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
]