from rest_framework import serializers
from reviews.models import Mouse, Keyboard, MouseReview, KeyboardReview


class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = '__all__'


class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__'


class MouseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MouseReview
        fields = '__all__'


class KeyboardReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyboardReview
        fields = '__all__'
