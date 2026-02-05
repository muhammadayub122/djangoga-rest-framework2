from django.shortcuts import render
from birinchi.models import Salom1, Salom2, Salom3, Salom4, Salom5
from birinchi.serializer import (
    Salom1Serializer,
    Salom2Serializer,
    Salom3Serializer,
    Salom4Serializer,
    Salom5Serializer,
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class Salom1ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom1Serializer
    queryset = Salom1.objects.all()


class Salom2ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom2Serializer
    queryset = Salom2.objects.all()


class Salom3ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom3Serializer
    queryset = Salom3.objects.all()


class Salom4ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom4Serializer
    queryset = Salom4.objects.all()


class Salom5ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom5Serializer
    queryset = Salom5.objects.all()

