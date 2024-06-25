from django.contrib import admin
from django.urls import path
#from django.conf.urls.static import static
#from django.conf import settings

# My sites
from .views import get_index, get_rcard

urlpatterns = [
    path('', get_index, name='index'),
    path('fn/get_rcard', get_rcard),
#    path('human', human),
]

#if settings.DEBUG:
#  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

