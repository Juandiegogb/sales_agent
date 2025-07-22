from rest_framework import routers
from .views import MiVista
from django.urls import include, path


router = routers.DefaultRouter()
router.register("", MiVista)


urlpatterns = [path("", include(router.urls))]
