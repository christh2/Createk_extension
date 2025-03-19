from django.urls import path, include
from analyser import views

urlpatterns = [
    path('phisher/', views.PhisherView.as_view(), name='phisher_view'),
    path('phisher/analyze-url/', views.analyze_url, name='analyze_url')
]
