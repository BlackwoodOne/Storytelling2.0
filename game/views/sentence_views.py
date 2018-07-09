from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Sentence
from ..forms import SentenceForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class SentenceListView(ListView):
    model = Sentence
    template_name = "game/sentence_list.html"
    paginate_by = 20
    context_object_name = "sentence_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SentenceListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SentenceListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SentenceListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SentenceListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SentenceListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SentenceListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SentenceListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SentenceListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SentenceListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SentenceListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SentenceListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SentenceListView, self).get_template_names()


class SentenceDetailView(DetailView):
    model = Sentence
    template_name = "game/sentence_detail.html"
    context_object_name = "sentence"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SentenceDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SentenceDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SentenceDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SentenceDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SentenceDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SentenceDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SentenceDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SentenceDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SentenceDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SentenceDetailView, self).get_template_names()


class SentenceCreateView(CreateView):
    model = Sentence
    form_class = SentenceForm
    # fields = ['content', 'valid', 'reject', 'game', 'createdBy']
    template_name = "game/sentence_create.html"
    success_url = reverse_lazy("sentence_list")

    def __init__(self, **kwargs):
        return super(SentenceCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SentenceCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SentenceCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SentenceCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SentenceCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SentenceCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SentenceCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SentenceCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SentenceCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SentenceCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SentenceCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SentenceCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SentenceCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:sentence_detail", args=(self.object.pk,))


class SentenceUpdateView(UpdateView):
    model = Sentence
    form_class = SentenceForm
    # fields = ['content', 'valid', 'reject', 'game', 'createdBy']
    template_name = "game/sentence_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "sentence"

    def __init__(self, **kwargs):
        return super(SentenceUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SentenceUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SentenceUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SentenceUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SentenceUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SentenceUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SentenceUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SentenceUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SentenceUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SentenceUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SentenceUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SentenceUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SentenceUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SentenceUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SentenceUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SentenceUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SentenceUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:sentence_detail", args=(self.object.pk,))


class SentenceDeleteView(DeleteView):
    model = Sentence
    template_name = "game/sentence_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "sentence"

    def __init__(self, **kwargs):
        return super(SentenceDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SentenceDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SentenceDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SentenceDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SentenceDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SentenceDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SentenceDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SentenceDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SentenceDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SentenceDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SentenceDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:sentence_list")
