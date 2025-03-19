from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
# Create your views here.

class CheckURL(APIView):
    def get(self, request: Request):
        return Response({
            "message": "OK"
        }, status=200)
