from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from django.db import connection
from pprint import pprint


class SearchProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related("brand", "group").all()
        serializer = ProductSerializer(products, many=True)
        data = serializer.data

        for q in connection.queries:
            pprint(q["sql"])

        return Response(data)
