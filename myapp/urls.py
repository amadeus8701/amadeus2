from django.urls import path
from myapp.views import display_text_file

urlpatterns = [
    path('', display_text_file, name='display_text_file'),
]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.serve_image, name='serve_image'),
]