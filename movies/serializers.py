from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    name_original = serializers.CharField(max_length=200)
