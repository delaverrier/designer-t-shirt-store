from channels.generic.websocket import AsyncWebsocketConsumer
import json
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'support'  # Имя комнаты (чата)
        self.room_group_name = f'chat_{self.room_name}'

        # Присоединяем клиента к комнате
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Отсоединяем клиента от комнаты
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Обработка входящего сообщения
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправка сообщения в комнату
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Отправка сообщения обратно клиенту
        message = event['message']

        # Отправка сообщения через WebSocket соединение
        await self.send(text_data=json.dumps({
            'message': message
        }))


