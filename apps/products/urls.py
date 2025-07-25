from rest_framework import routers
from .views import ShowProducts, SearchProducts
from django.urls import path


router = routers.DefaultRouter()


urlpatterns = [
    path("", ShowProducts.as_view()),
    path("search", SearchProducts.as_view()),
]
