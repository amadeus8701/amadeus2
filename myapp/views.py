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
from datetime import datetime

# ...

def serve_image(request):
    image_path = '/home/ubuntu/srv/screenshot.jpg'  # JPG 파일의 경로
    with open(image_path, 'rb') as image_file:
        response = HttpResponse(image_file.read(), content_type='image/jpeg')
    
    # 이미지 URL에 랜덤 파라미터를 추가하여 캐시 무효화를 수행합니다
    response['Cache-Control'] = 'no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    response['Cache-Control'] = 'public, max-age=0'
    
    # 이미지의 최종 수정 시간을 설정하여 브라우저가 변경을 감지하도록 합니다
    image_modified_time = os.path.getmtime(image_path)
    response['Last-Modified'] = datetime.utcfromtimestamp(image_modified_time).strftime('%a, %d %b %Y %H:%M:%S GMT')

    return response
