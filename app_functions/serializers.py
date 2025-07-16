from rest_framework import serializers
from .models import *

class FunctionsFourierSerializer(serializers.Serializer):
    a0 = serializers.FloatField()
    a1 = serializers.FloatField()
    a2 = serializers.FloatField()
    a3 = serializers.FloatField()
    a4 = serializers.FloatField()
    b1 = serializers.FloatField()
    b2 = serializers.FloatField()
    b3 = serializers.FloatField()
    b4 = serializers.FloatField()
    l = serializers.FloatField()
    name = serializers.CharField()
    description = serializers.CharField()
    class Meta:
        fields = ['a0', 'a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'l', 'name', 'description']

    def create(self, validated_data):
        return FunctionFourierSeriesModel.objects.create(**validated_data)