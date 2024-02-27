from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134062ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134062", Testconnectors134062ViewSet, basename="testconnectors134062"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
