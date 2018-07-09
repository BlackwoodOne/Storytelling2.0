from django.conf.urls import url
from ..views import (WordCardListView, WordCardCreateView, WordCardDetailView,
                     WordCardUpdateView, WordCardDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        WordCardCreateView.as_view(),
        name="word_card_create"),

    url(r'^(?P<pk>\d+)/update/$',
        WordCardUpdateView.as_view(),
        name="word_card_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        WordCardDeleteView.as_view(),
        name="word_card_delete"),

    url(r'^(?P<pk>\d+)/$',
        WordCardDetailView.as_view(),
        name="word_card_detail"),

    url(r'^$',
        WordCardListView.as_view(),
        name="word_card_list"),
]
