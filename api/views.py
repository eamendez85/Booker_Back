from django.shortcuts import render
from rest_framework import api_view
from rest_framework.response import Response

@api_view(['GET'])
def user_api_view(request):
    if request.method == 'GET':
        user=0
