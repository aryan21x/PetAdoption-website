from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'React and Django Combined'})

def Home(request):
    return Response({'message': 'Welcome to the Django backend!'})