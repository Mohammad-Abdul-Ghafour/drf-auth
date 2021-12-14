from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import FavSerialzer
from .models import Favorite
from .permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user

# CR views
class FavList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly, )

# RUD view
class FavDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)