from rest_framework import serializers
from .models import Categroy,Brand,Product


class CategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categroy
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'