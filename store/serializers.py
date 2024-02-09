from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product,Variation,VariationManager
from category.models import Category,Subcategory

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'

class CategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields='__all__'

class SubcategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model= Subcategory
        fields='__all__'