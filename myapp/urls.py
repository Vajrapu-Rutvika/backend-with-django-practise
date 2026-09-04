from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('pass_change/',views.reset_pass,name="password_change"),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('addblog/',views.addblogpost,name="add_blog"),
    path('edit_blogpost/<int:post_id>/', views.edit_blogpost, name='edit_blog'),
    path('view_blogpost/<int:post_id>/', views.view_blogpost, name='view_blogpost'),
    path('delete_blogpost/<int:post_id>/', views.delete_blogpost, name='delete_blog'),
    path('posts_list/', views.posts_list, name='view_posts'),

 

]