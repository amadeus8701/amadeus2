from django.contrib import admin
from django.urls import path, include
from myapp.views import display_text_file, poll_file_content

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # myapp 앱의 URL을 포함합니다.
    path('poll_file/', poll_file_content, name='poll_file_content'),  # 새로운 URL 패턴 추가
]
