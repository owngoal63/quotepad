from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from boilerinfo.models import ProductPrice, Document, Profile
from .serializers import ProductPriceSerializer, DocumentSerializer, ProfileSerializer, UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)   # default is now in settings.py

class ProductPriceView(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


