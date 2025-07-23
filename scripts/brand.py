from apps.products.models import Brand, Group, Product
from django.db import connection
from uuid import UUID


def run():
    with connection.cursor() as cursor:
        cursor.execute("""
SELECT PRODUCTNAME AS NAME,PB.ID AS BRAND,MPC.DESCRIPTION
FROM MYNTRA_PRODUCTS_CATALOG MPC
left join PRODUCTS_BRAND PB on MPC.PRODUCTBRAND = pb.NAME
""")
        group = Group.objects.filter(
            id=UUID("b9d3a261-7a58-4eec-b525-deaf4fac7529")
        ).first()
        rows = cursor.fetchall()
        print(group)

        for name, brand, description in rows:
            brand = Brand.objects.filter(id=brand).first()
            Product.objects.create(
                name=name, brand=brand, description=description, group=group
            )
