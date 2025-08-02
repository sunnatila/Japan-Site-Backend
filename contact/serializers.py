from .models import Contact
from rest_framework import serializers
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?[\d\s\-().]{7,20}$',
    message="The phone number is in the wrong format."
)

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    phone_number = serializers.CharField(validators=[phone_regex])
    message = serializers.CharField(required=True)


    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'message']
