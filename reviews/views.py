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
        queryset = None

        if 'brand' in request.query_params:
            queryset = Mouse.objects.filter(company__iexact=request.query_params.get('brand'))

        if 'button_count' in request.query_params:
            queryset = Mouse.objects.filter(button_count=request.query_params.get('amount'))

        return Response(data=MouseSerializer(queryset, many=True).data)

class KeyboardViewset(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

    @action(detail=False, methods=['GET'])
    def sort(self, request):
        queryset = None
        if 'brand' in request.query_params:
            queryset = Keyboard.objects.filter(company__iexact=request.query_params.get('brand'))

        if 'backlit' in request.query_params:
            queryset = Keyboard.objects.filter(is_backlit=request.query_params.get('backlit'))

        return Response(data=KeyboardSerializer(queryset, many=True).data)

class MouseReviewViewset(viewsets.ModelViewSet):
    queryset = MouseReview.objects.all()
    serializer_class = MouseReviewSerializer

    @action(detail=False, methods=['GET'])
    def sort(self, request):
        queryset = None

        if 'author' in request.query_params:
            queryset = MouseReview.objects.filter(author__iexact=request.query_params.get('author'))

        if 'brand' in request.query_params:
            queryset = MouseReview.objects.filter(
                mouse__company__iexact=request.query_params.get('brand'))

        return Response(data=MouseReviewSerializer(queryset, many=True).data)



class KeyboardReviewViewset(viewsets.ModelViewSet):
    queryset = KeyboardReview.objects.all()
    serializer_class = KeyboardReviewSerializer

    @action(detail=False, methods=['GET'])
    def sort(self, request):
        queryset = None

        if 'author' in request.query_params:
            queryset = KeyboardReview.objects.filter(author__iexact=request.query_params.get('author'))

        if 'brand' in request.query_params:
            queryset = KeyboardReview.objects.filter(
                keyboard__company__iexact=request.query_params.get('brand'))

        return Response(data=KeyboardReviewSerializer(queryset, many=True).data)
