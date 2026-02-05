from rest_framework.viewsets import ModelViewSet
from tortinchi.models import Salom1, Salom2, Salom3, Salom4, Salom5
from  tortinchi.serializer import (
    Salom1Serializer,
    Salom2Serializer,
    Salom3Serializer,
    Salom4Serializer,
    Salom5Serializer,
)

# Your views is here


class Salom1ViewSet(ModelViewSet):
    queryset = Salom1.objects.all()
    serializer_class = Salom1Serializer


class Salom2ViewSet(ModelViewSet):
    queryset = Salom2.objects.all()
    serializer_class = Salom2Serializer


class Salom3ViewSet(ModelViewSet):
    queryset = Salom3.objects.all()
    serializer_class = Salom3Serializer


class Salom4ViewSet(ModelViewSet):
    queryset = Salom4.objects.all()
    serializer_class = Salom4Serializer


class Salom5ViewSet(ModelViewSet):
    queryset = Salom5.objects.all()
    serializer_class = Salom5Serializer