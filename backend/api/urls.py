from django.urls import path
from .views import CheckURL

urlpatterns = [
    path("url-check/", CheckURL.as_view(), name="check-url")
]
