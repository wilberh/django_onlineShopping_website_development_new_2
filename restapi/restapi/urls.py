from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^gettalks$',views.gettalks,name='gettalks'),
    url(r'^gettalk/(?P<pk>\d+)$',views.gettalk,name='gettalk'),
    url(r'^insert$',views.insert,name='insert'),
    url(r'^update/(?P<pk>\d+)$',views.update,name='update'),
    url(r'^delete/(?P<pk>\d+)$',views.delete,name='delete'),
]
