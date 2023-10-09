from django.urls import path
from . import views
from myapp.views import display_text_file

urlpatterns = [
    path('image/', views.serve_image, name='serve_image'),  # 이미지 표시 URL
    path('text/', display_text_file, name='display_text_file'),  # 텍스트 파일 표시 URL
]