from rest_framework import serializers

from .models import AbandonedDog, Image

class DogImagesSerializer(serializers.ModelSerializer):
    images = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = '__all__'

class DogSerializer(serializers.ModelSerializer):
    images = DogImagesSerializer(read_only=True)
    class Meta:
        model = AbandonedDog
        fields = ['id', 'name', 'gender', 'datetime', 'weight', 'info', 'region', 'images']