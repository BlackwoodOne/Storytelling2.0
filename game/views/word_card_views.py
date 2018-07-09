from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import WordCard
from ..forms import WordCardForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class WordCardListView(ListView):
    model = WordCard
    template_name = "game/word_card_list.html"
    paginate_by = 20
    context_object_name = "word_card_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(WordCardListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(WordCardListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(WordCardListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(WordCardListView, self).get_queryset()

    def get_allow_empty(self):
        return super(WordCardListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(WordCardListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(WordCardListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(WordCardListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(WordCardListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(WordCardListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(WordCardListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WordCardListView, self).get_template_names()


class WordCardDetailView(DetailView):
    model = WordCard
    template_name = "game/word_card_detail.html"
    context_object_name = "word_card"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(WordCardDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(WordCardDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(WordCardDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(WordCardDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(WordCardDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(WordCardDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(WordCardDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(WordCardDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(WordCardDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WordCardDetailView, self).get_template_names()


class WordCardCreateView(CreateView):
    model = WordCard
    form_class = WordCardForm
    # fields = ['content', 'deckNumber', 'used', 'game', 'createdBy', 'onPlayerHand']
    template_name = "game/word_card_create.html"
    success_url = reverse_lazy("word_card_list")

    def __init__(self, **kwargs):
        return super(WordCardCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(WordCardCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(WordCardCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(WordCardCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(WordCardCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(WordCardCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(WordCardCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(WordCardCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(WordCardCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(WordCardCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(WordCardCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(WordCardCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WordCardCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:word_card_detail", args=(self.object.pk,))


class WordCardUpdateView(UpdateView):
    model = WordCard
    form_class = WordCardForm
    # fields = ['content', 'deckNumber', 'used', 'game', 'createdBy', 'onPlayerHand']
    template_name = "game/word_card_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "word_card"

    def __init__(self, **kwargs):
        return super(WordCardUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(WordCardUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(WordCardUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(WordCardUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(WordCardUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(WordCardUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(WordCardUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(WordCardUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(WordCardUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(WordCardUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(WordCardUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(WordCardUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(WordCardUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(WordCardUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(WordCardUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(WordCardUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WordCardUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:word_card_detail", args=(self.object.pk,))


class WordCardDeleteView(DeleteView):
    model = WordCard
    template_name = "game/word_card_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "word_card"

    def __init__(self, **kwargs):
        return super(WordCardDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(WordCardDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(WordCardDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(WordCardDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(WordCardDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(WordCardDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(WordCardDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(WordCardDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(WordCardDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(WordCardDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WordCardDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:word_card_list")
