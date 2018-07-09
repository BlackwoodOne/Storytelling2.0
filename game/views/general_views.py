from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from ..models import Game

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
       # Game.objects.all().delete()
        latest_games_list = Game.objects.order_by('-createdAt')[:5]

        context = {'latest_games_list': latest_games_list,}
        return render(request, 'index.html', context)


class AboutPageView(TemplateView):
    template_name = "about.html"