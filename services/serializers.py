from rest_framework.serializers import ModelSerializer
from .models import Service

class ServiceSerializer(ModelSerializer):

    class Meta:
        model = Service
        fields = ['id', 'title', 'description']


