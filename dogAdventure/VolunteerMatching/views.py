from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from django.db.models import Q

from .models import AbandonedDog
from .serializers import DogSerializer, DogListSerializer

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
        transport = request.GET.get("transport", None)
        destination = request.GET.get("destination", None)

        date = datetime.datetime.strptime(date + " 00:00:00", '%Y-%m-%d %H:%M:%S')
        if AbandonedDog.objects.filter(Q(datetime=date) & Q(transport=transport) & Q(destination=destination)).exists():
            dog = AbandonedDog.objects.filter(Q(datetime=date) & Q(transport=transport) & Q(destination=destination))
            serializer = DogListSerializer(dog, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class ReserveAPI(APIView):
    def post(self, request):
        id = request.data.get("id")
        data = {'id': id}
        return Response(data)
