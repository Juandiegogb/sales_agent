from django.db import models
from uuid import uuid4


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)


class Group(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)


class Rag(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    table = models.CharField(max_length=40)
    record = models.UUIDField()
    context = models.TextField()
    metadata = models.JSONField()
