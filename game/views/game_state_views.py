from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import GameState
from ..forms import GameStateForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class GameStateListView(ListView):
    model = GameState
    template_name = "game/game_state_list.html"
    paginate_by = 20
    context_object_name = "game_state_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(GameStateListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GameStateListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GameStateListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(GameStateListView, self).get_queryset()

    def get_allow_empty(self):
        return super(GameStateListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(GameStateListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(GameStateListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(GameStateListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(GameStateListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(GameStateListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(GameStateListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameStateListView, self).get_template_names()


class GameStateDetailView(DetailView):
    model = GameState
    template_name = "game/game_state_detail.html"
    context_object_name = "game_state"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(GameStateDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GameStateDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GameStateDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GameStateDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(GameStateDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(GameStateDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GameStateDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GameStateDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GameStateDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameStateDetailView, self).get_template_names()


class GameStateCreateView(CreateView):
    model = GameState
    form_class = GameStateForm
    # fields = ['name']
    template_name = "game/game_state_create.html"
    success_url = reverse_lazy("game_state_list")

    def __init__(self, **kwargs):
        return super(GameStateCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(GameStateCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GameStateCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GameStateCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(GameStateCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GameStateCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GameStateCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GameStateCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(GameStateCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GameStateCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GameStateCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(GameStateCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameStateCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:game_state_detail", args=(self.object.pk,))


class GameStateUpdateView(UpdateView):
    model = GameState
    form_class = GameStateForm
    # fields = ['name']
    template_name = "game/game_state_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "game_state"

    def __init__(self, **kwargs):
        return super(GameStateUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GameStateUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GameStateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GameStateUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GameStateUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(GameStateUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(GameStateUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(GameStateUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GameStateUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GameStateUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GameStateUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(GameStateUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GameStateUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GameStateUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GameStateUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GameStateUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameStateUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:game_state_detail", args=(self.object.pk,))


class GameStateDeleteView(DeleteView):
    model = GameState
    template_name = "game/game_state_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "game_state"

    def __init__(self, **kwargs):
        return super(GameStateDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GameStateDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(GameStateDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(GameStateDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GameStateDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(GameStateDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(GameStateDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GameStateDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GameStateDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GameStateDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameStateDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:game_state_list")
