from django.shortcuts import render

def display_text_file(request):
    with open('/home/ubuntu/srv/text_file.txt', 'r') as file:
        content = file.read()
    return render(request, 'myapp/index.html', {'content': content})

from django.http import JsonResponse

def poll_file_content(request):
    with open('/home/ubuntu/srv/text_file.txt', 'r') as file:
        content = file.read()
    return JsonResponse({'content': content})

from django.db import models

class UserInput(models.Model):
    input_text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

from django.shortcuts import render
from .models import UserInputModel

def display_inputs(request):
    inputs = UserInput.objects.all().order_by('-timestamp')
    return render(request, 'myapp/index.html', {'inputs': inputs})