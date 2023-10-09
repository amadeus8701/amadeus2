from django.contrib import admin
from django.urls import path, include
from myapp.views import display_text_file, poll_file_content, serve_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_text_file, name='display_text_file'),
    path('screenshot.jpg', serve_image, name='serve_image'),
    path('poll_file/', poll_file_content, name='poll_file_content'),
]