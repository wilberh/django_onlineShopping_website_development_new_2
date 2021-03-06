from tastypie.resources import ModelResource
from api.models import Talk
from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie.exceptions import InvalidFilterError
from django.template.defaultfilters import slugify
#import datetime

#This APP "api", uses the "Tastypi" RESTful package

from tastypie.authorization import Authorization

class AuthenticationMixin(object):
	def __init__(self):
		self._meta.authentication = ApiKeyAuthentication()
		self._meta.authorization = DjangoAuthorization()
		super(AuthenticationMixin, self).__init__

class GetTalks(ModelResource):
	class Meta:
		queryset =  Talk.objects.all()
		allowed_methods = ['get',]
		resource_name = 'gettalks'
		authorization = Authorization()

class GetTalk(ModelResource):
	class Meta:
		queryset =  Talk.objects.all()
		allowed_methods = ['get',]
		resource_name = 'gettalk'
		authorization = Authorization()

class Insert(ModelResource):
	class Meta:
		queryset =  Talk.objects.all()
		allowed_methods = ['post',]
		resource_name = 'insert'
		authorization = Authorization()

class Update(ModelResource):
	class Meta:
		queryset =  Talk.objects.all()
		allowed_methods = ['put',]
		resource_name = 'update'
		authorization = Authorization()

class Delete(ModelResource):
	class Meta:
		queryset =  Talk.objects.all()
		allowed_methods = ['delete',]
		resource_name = 'delete'
		authorization = Authorization()

v1_api = Api(api_name='v1')
v1_api.register(GetTalks())
v1_api.register(GetTalk())
v1_api.register(Insert())
v1_api.register(Update())
v1_api.register(Delete())