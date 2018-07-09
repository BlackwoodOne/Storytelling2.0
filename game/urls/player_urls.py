from django.conf.urls import url
from ..views import (PlayerListView, PlayerCreateView, PlayerDetailView,
                     PlayerUpdateView, PlayerDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        PlayerCreateView.as_view(),
        name="player_create"),

    url(r'^(?P<pk>\d+)/update/$',
        PlayerUpdateView.as_view(),
        name="player_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        PlayerDeleteView.as_view(),
        name="player_delete"),

    url(r'^(?P<pk>\d+)/$',
        PlayerDetailView.as_view(),
        name="player_detail"),

    url(r'^$',
        PlayerListView.as_view(),
        name="player_list"),
]
