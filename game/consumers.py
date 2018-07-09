from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
# This example uses WebSocket consumer, which is synchronous, and so
# needs the async channel layer functions to be converted.
#from asgiref.sync import async_to_sync

class NewPlayerConsumer(WebsocketConsumer):

    def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.room_game_id = 'game_%s' % self.game_id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_game_id,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_game_id,
            self.channel_name
        )
        
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        gameStarted = text_data_json.get('gameStarted', False) #default is false

        if gameStarted:
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_game_id,
                {
                    'type': 'game_hasStarted',
                    'playerName': message
                }
            )
            return

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_game_id,
            {
                'type': 'game_playerJoins',
                'playerName': message
            }
        )

    # Receive message from room group
    def game_playerJoins(self, event):
        message = event['playerName']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'playerName': message
        }))
    
    # Receive message from room group
    def game_hasStarted(self, event):
        message = event['playerName']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'playerName': message,
            'gameStarted': True
        }))


class CollectConsumer(WebsocketConsumer):

    def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.room_game_id = 'game_collect_%s' % self.game_id
        print('game_collect_%s' % self.game_id)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_game_id,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_game_id,
            self.channel_name
        )
        
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        new_words = text_data_json.get('new_words', []) #default is false

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_game_id,
            {
                'type': 'game_newWords',
                'new_words': new_words
            }
        )
    
    # Receive message from room group
    def game_newWords(self, event):
        message = event['new_words']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'new_words': message
        }))