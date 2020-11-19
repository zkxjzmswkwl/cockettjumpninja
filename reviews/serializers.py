from rest_framework import serializers
from reviews.models import Mouse, Keyboard


class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = '__all__'


class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__'