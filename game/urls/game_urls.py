from django.conf.urls import url
from ..views import (GameListView, GameCreateView, GameDetailView,
                     GameUpdateView, GameDeleteView,GameLobbyView,GameJoinView,GamePlayCollectView,GamePlayWaitView, GamePlayGroundView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        GameCreateView.as_view(),
        name="game_create"),

    url(r'^(?P<pk>\d+)/update/$',
       GameUpdateView.as_view(),
        name="game_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        GameDeleteView.as_view(),
        name="game_delete"),

    url(r'^(?P<pk>\d+)/$',
        GameDetailView.as_view(),
        name="game_detail"),

    url(r'^(?P<pk>\d+)/join$',
        GameJoinView.as_view(),
        name="game_join"),

    url(r'^(?P<pk>\d+)/lobby/$',
        GameLobbyView.as_view(),
        name="game_lobby"),

    url(r'^(?P<pk>\d+)/game/$',
        GameDetailView.as_view(),
        name="game_game"),

    url(r'^$',
        GameListView.as_view(),
        name="game_list"),

    url(r'^(?P<pk>\d+)/play/collect$',
        GamePlayCollectView.as_view(),
        name="play_collect"),

    url(r'^(?P<pk>\d+)/play/wait$',
        GamePlayWaitView.as_view(),
        name="play_wait"),

    url(r'^(?P<pk>\d+)/play/ground$',
        GamePlayGroundView.as_view(),
        name="play_ground"),
]
