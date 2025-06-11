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


class ZeroNameNumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZeroNameNumModel
        fields = ['name', 'num']