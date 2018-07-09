from django.contrib import admin
from .models import Game, Player,Sentence,WordCard, GameState, RoundState

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Sentence)
admin.site.register(WordCard)
admin.site.register(GameState)
admin.site.register(RoundState)