# myapp/consumers.py

import os
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings

class FileChangeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.file_path = '/home/ubuntu/srv/text_file.txt'
        self.last_modified = 0

        while True:
            try:
                current_mtime = os.path.getmtime(self.file_path)
                if current_mtime != self.last_modified:
                    with open(self.file_path, 'r') as file:
                        content = file.read()
                        await self.send(text_data=content)
                    self.last_modified = current_mtime
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Error: {str(e)}")
                await asyncio.sleep(1)
