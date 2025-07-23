from rest_framework import routers
from .views import SearchProducts
from django.urls import include, path


router = routers.DefaultRouter()


urlpatterns = [path("", SearchProducts.as_view())]
