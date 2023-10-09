

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


    


from django.http import FileResponse
import os

def serve_image(request):
    image_path = '/home/ubuntu/srv/screenshot.jpg'  # 여러분의 JPEG 파일 경로
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            return FileResponse(f, content_type='image/jpeg')
    else:
        # 파일이 존재하지 않는 경우 처리
        return HttpResponse("이미지를 찾을 수 없습니다.", status=404)