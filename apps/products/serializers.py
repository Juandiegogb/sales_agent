from rest_framework import serializers
from .models import Product, Brand, Group, ProductType


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    group = GroupSerializer()
    product_type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = "__all__"
