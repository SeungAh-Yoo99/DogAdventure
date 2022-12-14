from rest_framework import serializers

from .models import AbandonedDog, Image

class DogImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Image
        fields = ['image', ]


class DogSerializer(serializers.ModelSerializer):
    images = DogImagesSerializer(many=True, read_only=True)

    class Meta:
        model = AbandonedDog
        fields = ['id', 'name', 'gender', 'datetime', 'title', 'weight', 'info', 'region', 'transport', 'destination', 'images', 'isSuccess']


class DogListSerializer(serializers.ModelSerializer):
    images = DogImagesSerializer(many=True, read_only=True)
    
    class Meta:
        model = AbandonedDog
        fields = ['id', 'name', 'gender', 'title', 'weight', 'images', 'isSuccess']