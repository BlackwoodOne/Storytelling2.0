from django.conf.urls import url
from ..views import (SentenceListView, SentenceCreateView, SentenceDetailView,
                     SentenceUpdateView, SentenceDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        SentenceCreateView.as_view(),
        name="sentence_create"),

    url(r'^(?P<pk>\d+)/update/$',
        SentenceUpdateView.as_view(),
        name="sentence_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        SentenceDeleteView.as_view(),
        name="sentence_delete"),

    url(r'^(?P<pk>\d+)/$',
        SentenceDetailView.as_view(),
        name="sentence_detail"),

    url(r'^$',
        SentenceListView.as_view(),
        name="sentence_list"),
]
