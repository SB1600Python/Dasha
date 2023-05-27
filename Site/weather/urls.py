from django.urls import path
from weather.views import search_weather


urlpatterns = [
    path('', search_weather, name ='weather')
]