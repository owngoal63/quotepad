from rest_framework import serializers
from django.contrib.auth.models import User
from boilerinfo.models import Document, ProductPrice, Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']

class ProductPriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['id', 'url', 'user', 'brand', 'model_name', 'product_code','price','product_image']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'url','first_name','last_name','email','company_name','telephone', 'quote_prefix', 'cur_quote_no']       


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = fields = ('id', 'url', 'user', 'document', 'description')


