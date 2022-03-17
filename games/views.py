from django.shortcuts import render
from rest_framework import generics
from .serializer import GameSerializer
from .models import Game

class GameList(generics.ListCreateAPIView):
  queryset = Game.objects.all()
  serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  serializer_class = GameSerializer
