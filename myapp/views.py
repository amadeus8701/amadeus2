from django.http import HttpResponse
from django.shortcuts import render
import os

def serve_screenshot(request):
    # Linux PC에서의 JPG 파일 경로
    screenshot_path = '/home/ubuntu/srv/screenshot.jpg'

    # 파일이 있는지 확인합니다.
    if os.path.exists(screenshot_path):
        # JPG 파일을 열고 제공합니다.
        with open(screenshot_path, 'rb') as file:
            return FileResponse(file)
    else:
        # 파일이 존재하지 않는 경우 처리합니다.
        return HttpResponse('파일을 찾을 수 없습니다', status=404)

def display_text_file(request, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return render(request, 'myapp/index.html', {'content': content})

def poll_file_content(request):
    text_file_path = '/home/ubuntu/srv/text_file.txt'
    with open(text_file_path, 'r') as file:
        content = file.read()

    # 파일 내용을 그대로 반환합니다.
    return HttpResponse(content, content_type='application/json')



    
