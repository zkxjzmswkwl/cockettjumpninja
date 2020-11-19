from django.shortcuts import render
from rest_framework import viewsets
from reviews.models import Mouse, Keyboard
from reviews.serializers import MouseSerializer, KeyboardSerializer


class MouseViewset(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer


class KeyboardViewset(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer