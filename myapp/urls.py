from django.urls import path
from myapp.views import display_text_file, serve_image

urlpatterns = [
    path('', display_text_file, name='display_text_file'),
    path('poll_file/', poll_file_content, name='poll_file_content'),
    path('screenshot.jpg', serve_image, name='serve_image'),  # JPG 파일을 서빙하는 URL 패턴 추가
]