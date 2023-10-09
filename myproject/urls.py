from django.contrib import admin
from django.urls import path, include
from myapp.views import display_text_file, poll_file_content  # 'poll_file_content' 뷰 함수 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # 'myapp.urls'를 include
    path('poll_file/', poll_file_content, name='poll_file_content'),  # 'poll_file_content' 함수를 URL 패턴에 추가
]