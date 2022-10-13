from rest_framework import serializers

from .models import AbandonedDog, Image

class DogImagesSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Image
        fields = ['image', ]
    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

class DogSerializer(serializers.ModelSerializer):
    images = DogImagesSerializer(many=True, read_only=True)
    
    class Meta:
        model = AbandonedDog
        fields = ['id', 'name', 'gender', 'datetime', 'title', 'weight', 'info', 'region', 'transport', 'destination', 'images']


class DogListSerializer(serializers.ModelSerializer):
    images = DogImagesSerializer(many=True, read_only=True)
    
    class Meta:
        model = AbandonedDog
        fields = ['id', 'name', 'gender', 'title', 'weight', 'images']