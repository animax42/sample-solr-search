#inbuilt python imports

#inbuilt django imports
from django.shortcuts import render
from django.template import RequestContext

#local imports
from forms import CustomSearchForm
from django.views.generic import View

#inter-app imports

#third-party imports
from haystack.views import SearchView, FacetedSearchView
from haystack.query import SearchQuerySet


class CustomSearchView(FacetedSearchView):

    template = "search/search.html"

    def __init__(self):
        self.searchqueryset = SearchQuerySet().facet('author')
        self.load_all = True
        self.form_class = CustomSearchForm
        self.context_class = RequestContext
        self.results_per_page = 10

    def build_form(self,form_kwargs=None):
        if form_kwargs == None:
            form_kwargs = {}
        if self.request.GET.get('selected_facets'):
            form_kwargs['selected_facets'] = self.request.GET.getlist('selected_facets')
        # import ipdb; ipdb.set_trace();
        return super(FacetedSearchView, self).build_form(form_kwargs)
