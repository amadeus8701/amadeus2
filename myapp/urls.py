# viewer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_file, name='show_file'),
]