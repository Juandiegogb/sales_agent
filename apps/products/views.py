from django.shortcuts import render
from .models import Product
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


class MiVista(APIView):
    def get(self, request):
        data = {"mensaje": "Hola desde una vista personalizada"}
        return Response(data)
