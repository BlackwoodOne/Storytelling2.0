from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import RoundState
from ..forms import RoundStateForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class RoundStateListView(ListView):
    model = RoundState
    template_name = "game/round_state_list.html"
    paginate_by = 20
    context_object_name = "round_state_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RoundStateListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RoundStateListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RoundStateListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RoundStateListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RoundStateListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RoundStateListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RoundStateListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RoundStateListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RoundStateListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RoundStateListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RoundStateListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RoundStateListView, self).get_template_names()


class RoundStateDetailView(DetailView):
    model = RoundState
    template_name = "game/round_state_detail.html"
    context_object_name = "round_state"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RoundStateDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RoundStateDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RoundStateDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RoundStateDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RoundStateDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RoundStateDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RoundStateDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RoundStateDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RoundStateDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RoundStateDetailView, self).get_template_names()


class RoundStateCreateView(CreateView):
    model = RoundState
    form_class = RoundStateForm
    # fields = ['name']
    template_name = "game/round_state_create.html"
    success_url = reverse_lazy("round_state_list")

    def __init__(self, **kwargs):
        return super(RoundStateCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RoundStateCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RoundStateCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RoundStateCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RoundStateCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RoundStateCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RoundStateCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RoundStateCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RoundStateCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RoundStateCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RoundStateCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RoundStateCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RoundStateCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:round_state_detail", args=(self.object.pk,))


class RoundStateUpdateView(UpdateView):
    model = RoundState
    form_class = RoundStateForm
    # fields = ['name']
    template_name = "game/round_state_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "round_state"

    def __init__(self, **kwargs):
        return super(RoundStateUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RoundStateUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RoundStateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RoundStateUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RoundStateUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RoundStateUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RoundStateUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RoundStateUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RoundStateUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RoundStateUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RoundStateUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RoundStateUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RoundStateUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RoundStateUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RoundStateUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RoundStateUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RoundStateUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:round_state_detail", args=(self.object.pk,))


class RoundStateDeleteView(DeleteView):
    model = RoundState
    template_name = "game/round_state_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "round_state"

    def __init__(self, **kwargs):
        return super(RoundStateDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RoundStateDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RoundStateDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RoundStateDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RoundStateDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RoundStateDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RoundStateDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RoundStateDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RoundStateDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RoundStateDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RoundStateDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:round_state_list")
