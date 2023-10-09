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




from django.http import HttpResponse
import os
import random

# ...

def serve_image(request):
    image_path = '/home/ubuntu/srv/screenshot.jpg'
    with open(image_path, 'rb') as image_file:
        response = HttpResponse(image_file.read(), content_type='image/jpeg')
    
    # 더 강력한 캐시 무효화 헤더를 설정합니다
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    # 랜덤 파라미터를 이미지 URL에 추가하여 캐시 무효화를 수행합니다
    image_url = reverse('serve_image')
    image_url += f'?{random.randint(0, 100000)}'  # 랜덤 파라미터를 추가합니다
    response['Location'] = image_url

    return response