from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from reviews.models import Mouse, Keyboard, MouseReview, KeyboardReview
from reviews.serializers import MouseSerializer, KeyboardSerializer, MouseReviewSerializer, KeyboardReviewSerializer


class MouseViewset(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

    @action(detail=False, methods=['GET'])
    def sort(self, request):
        if 'brand' in request.query_params:
            queryset = Mouse.objects.filter(company__iexact=request.query_params.get('brand'))
            serializer = MouseSerializer(queryset, many=True)
            return Response(data=serializer.data)

        if 'button_count' in request.query_params:
            queryset = Mouse.objects.filter(button_count=request.query_params.get('amount'))
            serializer = MouseSerializer(queryset, many=True)
            return Response(data=serializer.data)


class KeyboardViewset(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

    @action(detail=False, methods=['GET'])
    def sort(self, request):
        if 'brand' in request.query_params:
            queryset = Keyboard.objects.filter(company__iexact=request.query_params.get('brand'))
            serializer = KeyboardSerializer(queryset, many=True)
            return Response(data=serializer.data)

        if 'backlit' in request.query_params:
            queryset = Keyboard.objects.filter(is_backlit=request.query_params.get('backlit'))
            serializer = KeyboardSerializer(queryset, many=True)
            return Response(data=serializer.data)


class MouseReviewViewset(viewsets.ModelViewSet):
    queryset = MouseReview.objects.all()
    serializer_class = MouseReviewSerializer


class KeyboardReviewViewset(viewsets.ModelViewSet):
    queryset = KeyboardReview.objects.all()
    serializer_class = KeyboardReviewSerializer

