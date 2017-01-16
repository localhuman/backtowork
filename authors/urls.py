from django.conf.urls import url,include
from django.contrib import admin

from .views import *

urlpatterns = [

    url(r'^$', home,name='home'),
    url(r'^author/(?P<pk>[0-9]+)/$', author_detail, name='author_detail'),
    url(r'^author/(?P<pk>[0-9]+)/syncfollow$', follow_authors, name='followauthors'),

    url(r'^author/tweet$', author_tweet, name='author_tweet'),

    #    url(r'^make$', make_poo, name='poo_make'),
#    url(r'^(?P<pk>[0-9]+)/$', poo_detail, name='poo_detail'),
#    url(r'^(?P<pk>[0-9]+)/edit$', edit_poo, name='poo_upate'),
#    url(r'^(?P<pk>[0-9]+)/flush$', delete_poo, name='poo_delete'),

#    url(r'^(?P<pk>[0-9]+)/fav/$', add_tp, name='add_tp'),

#    url(r'^(?P<pk>[0-9]+)/flag/$', flag_poo, name='poo_flag'),

]
