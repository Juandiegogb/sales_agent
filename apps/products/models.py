from django.db import models
from uuid import uuid4


class Company(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.TextField()
    city = models.CharField(max_length=100)
    industry = models.CharField(
        choices=[("TEX", "Textil"), ("O&L", "Oil & gas"), ("SW", "Software")]
    )


class Member(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class Group(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)


class ProductType(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock = models.PositiveSmallIntegerField(default=0)


class Rag(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    table = models.CharField(max_length=40)
    record = models.UUIDField()
    context = models.TextField()
    metadata = models.JSONField()
