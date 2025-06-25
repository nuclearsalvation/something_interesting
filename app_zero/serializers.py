from rest_framework import serializers
from .models import ZeroNameNumModel

class ZeroSerializer(serializers.Serializer):
    source = serializers.CharField()

class ZeroResponseSerializer(serializers.Serializer):
    a = serializers.FloatField()
    b = serializers.FloatField()
    c = serializers.FloatField()
    dx = serializers.FloatField()
    fin = serializers.IntegerField()
    class Meta:
        fields = ['a', 'b', 'c', 'dx', 'fin']


class ZeroNameNumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZeroNameNumModel
        fields = ['name', 'num']

class ZeroDampingSerializer(serializers.Serializer):
    a = serializers.FloatField()
    b = serializers.FloatField()
    c = serializers.FloatField()
    dx = serializers.FloatField()
    mu = serializers.FloatField()
    fin = serializers.IntegerField()
    class Meta:
        fields = ['a', 'b', 'c', 'dx', 'fin', 'mu']