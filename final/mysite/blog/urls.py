from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    # your code goes here
    url(r'^list$', views.list),
    # ex: /entry/5/
    url(r'^entry/(?P<entry_id>\d+)/$', views.detail),
    url(r'^entry/(?P<entry_id>\d+)/comment$', views.comment),
)
