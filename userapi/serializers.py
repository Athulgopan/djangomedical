from rest_framework import serializers
from tablemedicine.models import medkit

class useapiSerializer(serializers.ModelSerializer):
     class Meta:
        model = medkit
        fields = '__all__'