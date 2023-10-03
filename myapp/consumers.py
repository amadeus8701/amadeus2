import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class FileChangeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_file_change_notification(self, event):
        await self.send(text_data=json.dumps({
            'message': '파일이 변경되었습니다.'
        }))
