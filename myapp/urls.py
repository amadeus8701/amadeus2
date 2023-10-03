from django.urls import path
from . import views
from . import consumers

urlpatterns = [
    path('', views.display_file, name='display_file'),
]
