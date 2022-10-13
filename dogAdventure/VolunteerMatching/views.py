from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

from .models import AbandonedDog
from .serializers import DogSerializer

# Create your views here.
class TestAPI(APIView):
    def get(self, request):
        data = {'message': 'SUCCESS'}
        return Response(data)


class DogDetailAPI(APIView):
    def get(self, request):
        id = request.GET.get("id", None)
        dog = AbandonedDog.objects.get(id=id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)


class DogListFilteringAPI(APIView):
    def get(self, request):
        date = request.GET.get("date", None)
        date = datetime.datetime.strptime(date + " 00:00:00", '%Y-%m-%d %H:%M:%S')
        dog = AbandonedDog.objects.get(datetime=date)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

class ReAPI(APIView):
    def get(self, request):
        data = {'message': 'SUCCESS'}
        return Response(data)