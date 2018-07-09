from django.conf.urls import include, url

app_name="game"

urlpatterns = [
    url(r'^game_states/', include('game.urls.game_state_urls')),  # NOQA
    url(r'^round_states/', include('game.urls.round_state_urls')),
    url(r'^games/', include('game.urls.game_urls')),
    url(r'^players/', include('game.urls.player_urls')),
    url(r'^word_cards/', include('game.urls.word_card_urls')),
    url(r'^sentences/', include('game.urls.sentence_urls')),
    url(r'^', include('game.urls.general_urls'))
]
