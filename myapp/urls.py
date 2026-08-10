from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/',views.post_detail, name='post_detail'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
    path('product/', views.product_detail, name='product_detail'),
    path('welcome/', views.welcome, name='welcome'),
    path('item/', views.items_list, name='items_list'),
    path('posts_list/', views.posts_list, name='posts_list'),
]