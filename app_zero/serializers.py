from rest_framework import serializers

class ZeroSerializer(serializers.Serializer):
    source = serializers.CharField()