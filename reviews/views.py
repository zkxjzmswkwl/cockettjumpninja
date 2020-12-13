from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from reviews.models import Mouse, Keyboard
from reviews.serializers import MouseSerializer, KeyboardSerializer


class MouseViewset(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

    @action(detail=False, methods=['GET'])
    def by_brand(self, request):
        queryset = Mouse.objects.filter(company__iexact=request.query_params.get('brand'))
        serializer = MouseSerializer(queryset, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def by_button_count(self, request):
        queryset = Mouse.objects.filter(button_count=request.query_params.get('amount'))
        serializer = MouseSerializer(queryset, many=True)
        return Response(data=serializer.data)


class KeyboardViewset(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer
