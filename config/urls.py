"""
PROJECT LEVEL URLS 
"""
from django.contrib import admin
from django.urls import path
from acid.views import check_duplicates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_duplicates/', check_duplicates),
]
