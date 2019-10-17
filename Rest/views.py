from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from boilerinfo.models import ProductPrice, Document, Profile
from .serializers import ProductPriceSerializer, DocumentSerializer, ProfileSerializer, UserSerializer

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

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

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Rest/profile_list.html'

    def get(self, request):
        queryset = Profile.objects.all()
        return Response({'profiles': queryset})

class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Rest/profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')        


