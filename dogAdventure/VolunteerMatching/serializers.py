from rest_framework import serializers

from .models import AbandonedDog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedDog
        fields = '__all__'