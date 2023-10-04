# viewer/consumers.py
import asyncio
import os
import time
from channels.generic.websocket import AsyncWebsocketConsumer

class UpdateFileConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        file_path = '/home/ubuntu/srv/text_file.txt'
        while True:
            try:
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                await self.send(text_data=file_contents)
                await asyncio.sleep(1)  # 1초마다 파일 확인
            except Exception as e:
                print(f"Error reading file: {str(e)}")
                await asyncio.sleep(5)  # 오류 발생 시 5초 대기 후 다시 시도
