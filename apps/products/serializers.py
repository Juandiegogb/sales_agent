from rest_framework import serializers
from .models import Product, Brand, Group, Rag


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    group = GroupSerializer()

    class Meta:
        model = Product
        fields = "__all__"
