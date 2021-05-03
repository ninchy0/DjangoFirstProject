from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),
    path('blog-home', blog_home, name='blog-home'),
    path('blog-single', blog_single, name='blog-single'),
    path('elements', elements, name='elements')
]
