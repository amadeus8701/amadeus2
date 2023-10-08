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





from django.shortcuts import render, get_object_or_404
from .models import Image

def display_image(request):
    try:
        latest_image = Image.objects.latest('uploaded_at')
    except Image.DoesNotExist:
        latest_image = None
    
    return render(request, 'myapp/index.html', {'latest_image': latest_image})

from .forms import ImageForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    return render(request, 'myapp/index.html', {'form': form})



