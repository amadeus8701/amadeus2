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
from django.templatetags.static import static

def display_image(request):
    image_path = '/home/ubuntu/srv/screenshot.jpg'  # JPG 파일의 경로
    image_url = static(image_path)
    return render(request, 'myapp/index.html', {'image_url': image_url})

from django.shortcuts import render
from django.templatetags.static import static
from django.http import JsonResponse

def poll_image(request):
    image_path = '/home/ubuntu/srv/screenshot.jpg'  # JPG 파일의 경로
    image_url = static(image_path)
    return JsonResponse({'image_url': image_url})

from django.http import HttpResponse

def display_image(request):
    image_path = '/home/ubuntu/srv/screenshot.jpg'  # JPG 파일의 경로

    # 이미지 파일을 읽어옵니다.
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # MIME 타입을 'image/jpeg'로 설정하여 이미지 파일을 반환합니다.
    return HttpResponse(image_data, content_type='image/jpg')


