from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ai.invok_ai import phisher_ai
# Create your views here.

class CheckURL(APIView):
    def get(self, request: Request):
        url = request.data.get("url")
        res = phisher_ai(url)
        return Response({
            "message": "OK",
            "result": res
        }, status=200)
