from django.shortcuts import render

#This APP "restapi", uses the "djangorestframework" / Django RESTful package

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import Talk
from restapi.serializers import TalkSerializer
#import datetime

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

# GetTalks() -returns list of talks
@csrf_exempt
def gettalks(request):
	if request.method == 'GET':
		talks = Talk.objects.all()
		talks_serializer = TalkSerializer(talks, many=True)
		return JSONResponse(talks_serializer.data)

	else:
		return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

# GetTalk(int ID)
@csrf_exempt
def gettalk(request, pk):
	try:
		talk = Talk.objects.get(pk=pk)
	except Talk.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		talk_serializer = TalkSerializer(talk)
		return JSONResponse(talk_serializer.data)

	else:
		return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

# Insert(Talk)
@csrf_exempt
def insert(request):
	if request.method == 'POST':
		talk_data = JSONParser().parse(request)
		talk_serializer = TalkSerializer(data=talk_data)
		if talk_serializer.is_valid():
			talk_serializer.save()
			return JSONResponse(talk_serializer.data, status=status.HTTP_201_CREATED)
		return JSONResponse(talks_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	else:
		return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

# Update(Talk,ID)
@csrf_exempt
def update(request, pk):
	try:
		talk = Talk.objects.get(pk=pk)
	except Talk.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		talk_data = JSONParser().parse(request)
		talk_serializer = TalkSerializer(talk, data=talk_data)
		if talk_serializer.is_valid():
			talk_serializer.save()
			return JSONResponse(talk_serializer.data)
		return JSONResponse(talk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	else:
		return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

# Delete(ID)
@csrf_exempt
def delete(request, pk):
	try:
		talk = Talk.objects.get(pk=pk)
	except Talk.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'DELETE':
		talk.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)





