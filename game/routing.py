from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/lobby/(?P<game_id>[^/]+)/$', consumers.NewPlayerConsumer),
    url(r'^ws/collect/(?P<game_id>[^/]+)/$', consumers.CollectConsumer),
]