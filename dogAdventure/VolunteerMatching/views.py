from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

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
        dog = AbandonedDog.objects.get(date__lt=id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

class ReAPI(APIView):
    def get(self, request):
        data = {'message': 'SUCCESS'}
        return Response(data)