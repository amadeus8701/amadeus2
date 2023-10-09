from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.serve_image, name='serve_image'),  # 이미지 표시 URL
    path('text/', views.display_text_file, name='display_text_file'),  # 텍스트 파일 표시 URL
]