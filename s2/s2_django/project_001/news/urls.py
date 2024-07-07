from django.contrib import admin
from django.urls import path


# My sites
from .views import index, get_category

urlpatterns = [
    path('', index, name = 'home'),
    path('category/<int:cid>', get_category, name='category'),
]

