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
        dogs = AbandonedDog.objects.filter(id=id)
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)