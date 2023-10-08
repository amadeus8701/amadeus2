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





from django.core.files import File
from django.conf import settings
from .models import Image

def upload_image(request):
    if request.method == 'POST':
        title = request.POST['title']

        # 이미지 파일 경로
        image_path = '/home/ubuntu/srv/screenshot.jpg'

        # 이미지를 MEDIA_ROOT로 복사
        with open(image_path, 'rb') as img_file:
            image = Image(title=title)
            image.image_file.save('screenshot.jpg', File(img_file), save=True)

        return redirect('image_viewer:display_images')

    return render(request, 'upload_image.html')

from django.http import JsonResponse
import os

def poll_image(request):
    # 이미지 파일의 절대 경로를 설정합니다.
    image_path = '/home/ubuntu/srv/screenshot.jpg'

    # 파일 경로에서 파일 이름만 추출합니다.
    image_name = os.path.basename(image_path)

    # 이미지 파일의 절대 URL을 생성합니다.
    image_url = request.build_absolute_uri(image_name)

    # JSON 응답으로 이미지 URL을 반환합니다.
    return JsonResponse({'image_url': image_url})
