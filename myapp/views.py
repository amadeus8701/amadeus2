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


import os
from django.http import HttpResponse
from django.shortcuts import render

def display_image(request):
    image_path = '/home/ubuntu/srv/screenshot.jpg'
    return render(request, 'myapp/index.html', {'image_path': image_path})

def poll_image(request):
    image_path = '/home/ubuntu/srv/screenshot.jpg'
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    return HttpResponse(image_data, content_type='image/jpeg')