from rest_framework import serializers
from .models import *

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todo
        fields='__all__'