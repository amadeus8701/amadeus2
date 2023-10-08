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
from .models import Image

def display_image(request):
    images = Image.objects.all().order_by('-uploaded_at')[:5]
    return render(request, 'myapp/index.html', {'images': images})

from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def display_image(request):
    images = Image.objects.all().order_by('-uploaded_at')[:5]
    form = ImageForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('display_image')

    return render(request, 'myapp/index.html', {'images': images, 'form': form})