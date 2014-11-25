#inbuilt django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
#interapp imports
from myapp.views import CustomSearchView
from myapp.forms import CustomSearchForm

#third-party imports


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'solr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', CustomSearchView(), name='search'),
)
