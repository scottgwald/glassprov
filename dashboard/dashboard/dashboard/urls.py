from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

from .views import (
    home
)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^api/", include("voting.urls")),
    url(r'^dashboard/', TemplateView.as_view(template_name='admin.html'))
)
