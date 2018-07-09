from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Player
from ..forms import PlayerForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class PlayerListView(ListView):
    model = Player
    template_name = "game/player_list.html"
    paginate_by = 20
    context_object_name = "player_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PlayerListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlayerListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlayerListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PlayerListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PlayerListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PlayerListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PlayerListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PlayerListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PlayerListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PlayerListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PlayerListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlayerListView, self).get_template_names()


class PlayerDetailView(DetailView):
    model = Player
    template_name = "game/player_detail.html"
    context_object_name = "player"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PlayerDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlayerDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlayerDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlayerDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlayerDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PlayerDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlayerDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlayerDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlayerDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlayerDetailView, self).get_template_names()


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    # fields = ['name', 'playerPosition', 'playing', 'points', 'game', 'playerState']
    template_name = "game/player_create.html"
    success_url = reverse_lazy("player_list")

    def __init__(self, **kwargs):
        return super(PlayerCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PlayerCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlayerCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlayerCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PlayerCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlayerCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlayerCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlayerCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PlayerCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlayerCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlayerCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PlayerCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlayerCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:player_detail", args=(self.object.pk,))


class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    # fields = ['name', 'playerPosition', 'playing', 'points', 'game', 'playerState']
    template_name = "game/player_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "player"

    def __init__(self, **kwargs):
        return super(PlayerUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlayerUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlayerUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlayerUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlayerUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlayerUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PlayerUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PlayerUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlayerUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlayerUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlayerUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PlayerUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlayerUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlayerUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlayerUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlayerUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlayerUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:player_detail", args=(self.object.pk,))


class PlayerDeleteView(DeleteView):
    model = Player
    template_name = "game/player_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "player"

    def __init__(self, **kwargs):
        return super(PlayerDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlayerDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PlayerDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PlayerDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlayerDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlayerDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PlayerDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlayerDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlayerDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlayerDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlayerDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:player_list")
