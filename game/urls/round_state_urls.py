from django.conf.urls import url
from ..views import (RoundStateListView, RoundStateCreateView, RoundStateDetailView,
                     RoundStateUpdateView, RoundStateDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        RoundStateCreateView.as_view(),
        name="round_state_create"),

    url(r'^(?P<pk>\d+)/update/$',
        RoundStateUpdateView.as_view(),
        name="round_state_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        RoundStateDeleteView.as_view(),
        name="round_state_delete"),

    url(r'^(?P<pk>\d+)/$',
        RoundStateDetailView.as_view(),
        name="round_state_detail"),

    url(r'^$',
        RoundStateListView.as_view(),
        name="round_state_list"),
]
