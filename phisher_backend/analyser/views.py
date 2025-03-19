from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.renderers import JSONRenderer

class PhisherView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Phisher Detection API!"})

class phisher_view(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome to the Phisher Detection API!",
            "description": "This endpoint allows you to analyze URLs for potential phishing or malicious content.",
            "usage": {
                "method": "POST",
                "endpoint": "/analyze-url/",
                "parameters": {
                    "url": "The URL to be analyzed (required)"
                },
                "example_request": {
                    "url": "http://example.com"
                },
                "example_response": {
                    "url": "http://example.com",
                    "result": "safe"
                }
            }
        }
    )

def analyze_url(request):
    if request.method == 'POST':
        url = request.data.get('url')
        # Analyze the URL here
        return Response({
            "url": url,
            "result": "safe"
        })
