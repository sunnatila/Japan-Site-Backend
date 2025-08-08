from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product



class ProductsSerializer(ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

