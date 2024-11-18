from django.urls import path
from . import views

#app_name='blogs'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
   #  path('new/', views.blog_create, name='blog_create'),
     
   
   ]