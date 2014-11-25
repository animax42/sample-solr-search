#inbuilt python imports

#inbuilt django imports
from django import forms

#local imports

#inter-app imports

#third-party imports
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet, EmptySearchQuerySet

class CustomSearchForm(FacetedSearchForm):

    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(CustomSearchForm, self).search()
        # import ipdb; ipdb.set_trace();

        if not self.is_valid():
            return self.no_query_found()

        # Check to see if a start_date was chosen.

        if self.cleaned_data['q']:
            sqs = SearchQuerySet().facet('author')
            sqs_content = sqs.filter(content_auto=self.cleaned_data['q'])
            sqs_title = sqs.filter(title_auto=self.cleaned_data['q'])
            sqs = sqs_content|sqs_title

        if self.cleaned_data['start_date']:
            sqs = sqs.filter(pub_date__gte=self.cleaned_data['start_date'])

        # Check to see if an end_date was chosen.
        if self.cleaned_data['end_date']:
            sqs = sqs.filter(pub_date__lte=self.cleaned_data['end_date'])

        if self.selected_facets:
            faceted_query_set = EmptySearchQuerySet()
            for facet in self.selected_facets:
                if 'author' in facet:
                    author_exact = facet.split(':')
                    author_name = author_exact[len(author_exact)-1]
                    faceted_query_set = SearchQuerySet().filter(author=author_name)|faceted_query_set

            sqs = sqs&faceted_query_set


        return sqs
