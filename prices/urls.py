from django.conf.urls import patterns, url
from prices import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.product, name='product')
)