from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tortinchi.views import (
    Salom1ViewSet,
    Salom2ViewSet,
    Salom3ViewSet,
    Salom4ViewSet,
    Salom5ViewSet,
)

router = DefaultRouter()
router.register(r"1", Salom1ViewSet, basename="salom1")
router.register(r"2", Salom2ViewSet, basename="salom2")
router.register(r"3", Salom3ViewSet, basename="salom3")
router.register(r"4", Salom4ViewSet, basename="salom4")
router.register(r"5", Salom5ViewSet, basename="salom5")
urlpatterns = [
    path("", include(router.urls)),
]