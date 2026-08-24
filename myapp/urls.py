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
    path('one/', views.one_to_one_demo, name='one_to_one_demo'),
    path('many/', views.one_to_many_demo, name='one_to_many_demo'),
    path('manytomany/', views.many_to_many_demo, name='many_to_many_demo'),
    path('create_post/', views.create_post, name='create_post'),
    path('register/', views.register, name='register'),
    path('create_event/', views.create_event, name='create_event'),
    path('auth/', views.register_auth, name='register_auth'),
]