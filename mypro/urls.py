from django.contrib import admin
from django.urls import path
from mypro import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name='home'),

    path('contact/', views.contact, name='contact'),

    path('about/', views.About.as_view(), name='about'),

    path('user/<str:username>/', views.profile, name='profile'),

    path('product/<int:id>/', views.product, name='product'),

    path('blog/<slug:slug>/', views.blog, name='blog'),

    path('item/<uuid:item_id>/', views.item_detail, name='item_detail'),

    path('media/<path:path>/', views.media_handler, name='media_handler'),

    path('post/', views.go_to_post, name='go_to_post'),
]