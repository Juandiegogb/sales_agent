from django.contrib import admin
from .models import Brand, Group, Product, Rag, Company, Inventory, Member, ProductType


admin.site.register(
    [Brand, Group, Product, Rag, Company, Inventory, Member, ProductType]
)
