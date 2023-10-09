from django.urls import path
from myapp.views import serve_screenshot, display_text_file, poll_file_content

urlpatterns = [
    path('screenshot.jpg', serve_screenshot, name='serve_screenshot'),
    path('text_file', display_text_file, name='display_text_file'),
    path('poll_text_file', poll_file_content, name='poll_file_content'),
]

