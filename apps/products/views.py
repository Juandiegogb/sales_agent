from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from django.db import connection
from pprint import pprint
from .utils import search_product
from rest_framework import status


class ShowProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related("brand", "group").all()
        serializer = ProductSerializer(products, many=True)
        data = serializer.data

        for q in connection.queries:
            pprint(q["sql"])

        return Response(data)


class SearchProducts(APIView):
    def get(self, request):
        search_query = request.GET.get("search")

        if not search_query:
            return Response(
                "Search query params not found", status=status.HTTP_400_BAD_REQUEST
            )
        results = search_product(search_query)

        if not results:
            return Response("No products matched")
        return Response(results)
