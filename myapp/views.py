import json
import asyncio
from django.shortcuts import render
from django.http import HttpResponse
from channels.generic.websocket import AsyncWebsocketConsumer

def display_file(request):
    with open('/home/ubuntu/srv/text_file.txt', 'r') as file:
        content = file.read()
    return render(request, 'myapp/display_file.html', {'content': content})

class FileChangeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_file_change_notification(self, event):
        await self.send(text_data=json.dumps({
            'message': '파일이 변경되었습니다.'
        }))