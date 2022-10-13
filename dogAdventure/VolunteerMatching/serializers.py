from rest_framework import serializers

from .models import AbandonedDog, Image

class DogImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = ['id', 'dog', 'image']

class DogSerializer(serializers.ModelSerializer):
    images = DogImagesSerializer(many=True, read_only=True)
    class Meta:
        model = AbandonedDog
        fields = ['id', 'name', 'gender', 'datetime', 'weight', 'info', 'region', 'images']