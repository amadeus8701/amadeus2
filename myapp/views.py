# viewer/views.py
from django.shortcuts import render

def show_file(request):
    with open('/home/ubuntu/srv/text_file.txt', 'r') as file:
        file_contents = file.read()
    return render(request, 'myapp/display_file.html', {'file_contents': file_contents})