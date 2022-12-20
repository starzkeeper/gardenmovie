from django.shortcuts import render
from rest_framework import generics
import requests

from .serializers import MovieSerializer


class MovieAPI(generics.ListAPIView):
    queryset = requests.get('https://kinobd.ru/api/films').json()['data']
    serializer_class = MovieSerializer


