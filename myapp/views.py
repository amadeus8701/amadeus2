from django.shortcuts import render

def display_file(request):
    with open('/home/ubuntu/srv/text_file.txt', 'r') as file:
        lines = file.readlines()
    return render(request, 'myapp/display_file.html', {'lines': lines})