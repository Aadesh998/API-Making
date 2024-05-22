from rest_framework import serializers
from .models import *

class Advocateserializer(serializers.ModelSerializer):

    class Meta:
        model = Advocate
        fields = '__all__'