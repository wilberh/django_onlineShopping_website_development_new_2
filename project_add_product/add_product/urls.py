from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list,name='product_list'),
    url(r'^product/(?P<pk>\d+)$',views.product_details,name='product_details'),
    url(r'^product/new$',views.product_new,name='product_new'),
    url(r'^product/edit/(?P<pk>\d+)$',views.product_edit,name='product_edit'),
    url(r'^sendemail$',views.send_email,name='send_email'),
    url(r'^sendemail_thanks$',views.sendemail_thanks,name='sendemail_thanks'),
]
