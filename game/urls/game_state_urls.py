from django.conf.urls import url
from ..views import (GameStateListView, GameStateCreateView, GameStateDetailView,
                     GameStateUpdateView, GameStateDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        GameStateCreateView.as_view(),
        name="game_state_create"),

    url(r'^(?P<pk>\d+)/update/$',
        GameStateUpdateView.as_view(),
        name="game_state_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        GameStateDeleteView.as_view(),
        name="game_state_delete"),

    url(r'^(?P<pk>\d+)/$',
        GameStateDetailView.as_view(),
        name="game_state_detail"),

    url(r'^$',
        GameStateListView.as_view(),
        name="game_state_list"),
]
