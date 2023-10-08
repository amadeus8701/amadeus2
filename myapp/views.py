from django.shortcuts import render

def display_text_file(request):
    with open('/home/ubuntu/srv/text_file.txt', 'r') as file:
        content = file.read()
    return render(request, 'myapp/index.html', {'content': content})

from django.http import HttpResponse

def poll_file_content(request):
    with open('/home/ubuntu/srv/text_file.txt', 'r') as file:
        content = file.read()

    # 파일 내용을 그대로 반환합니다.
    return HttpResponse(content, content_type='application/json')

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os

def upload(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)

        # 파일 이름과 경로를 로그 파일에 기록합니다.
        log_file_path = os.path.join(MEDIA_ROOT, 'uploads.log')
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"File: {filename}, Path: {uploaded_file_url}\n")

    # 로그에서 업로드된 파일 목록을 가져옵니다.
    log_contents = []
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            log_contents = log_file.readlines()

    # 가장 최근 파일을 표시합니다.
    latest_file = uploaded_file_url if 'uploaded_file_url' in locals() else None

    return render(request, 'index.html', {'log_contents': log_contents, 'latest_file': latest_file})
