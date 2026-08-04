from django.urls import path
from mypro import views

urlpatterns = [
    path('',views.home,name='home',)
]