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
    
class FunctionsTaylorSerializer(serializers.Serializer):
    c0 = serializers.FloatField()
    c1 = serializers.FloatField()
    c2 = serializers.FloatField()
    c3 = serializers.FloatField()
    c4 = serializers.FloatField()
    c5 = serializers.FloatField()
    c6 = serializers.FloatField()
    c7 = serializers.FloatField()
    c8 = serializers.FloatField()
    x0 = serializers.FloatField()
    name = serializers.CharField()
    description = serializers.CharField()
    class Meta:
        fields = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'x0', 'name', 'description']

    def create(self, validated_data):
        return FunctionsTaylorSeriesModel.objects.create(**validated_data)