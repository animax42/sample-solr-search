import datetime
from haystack import indexes
from myapp.models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user',faceted=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    content_auto = indexes.EdgeNgramField(model_attr='body')
    title_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
