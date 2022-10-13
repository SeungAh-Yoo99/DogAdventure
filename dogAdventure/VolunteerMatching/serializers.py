from rest_framework import serializers

from .models import AbandonedDog, Image

class DogImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Image
        fields = ['image', ]


class DogSerializer(serializers.ModelSerializer):
    # images = serializers.SerializerMethodField()
    images = DogImagesSerializer(many=True, read_only=True)

    def get_images(self, obj):
        image=obj.image.all()
        return DogImagesSerializer(instance=image, many=True, context=self.context).data
    def create(self, validated_data):
        instance = AbandonedDog.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            Image.objects.create(diary=instance, image=image_data)
        return instance
    class Meta:
        model = AbandonedDog
        fields = ['id', 'name', 'gender', 'datetime', 'title', 'weight', 'info', 'region', 'transport', 'destination', 'images']


class DogListSerializer(serializers.ModelSerializer):
    images = DogImagesSerializer(many=True, read_only=True)
    
    class Meta:
        model = AbandonedDog
        fields = ['id', 'name', 'gender', 'title', 'weight', 'images']