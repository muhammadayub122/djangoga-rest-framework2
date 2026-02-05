from django.urls import path
from ikkinchi.views import Salom1ListCreateApiView,Salom2ListCreateApiView,Salom3ListCreateApiView,Salom4ListCreateApiView,Salom5ListCreateApiView

urlpatterns = [
    path('1/',Salom1ListCreateApiView.as_view()),
    path('2/',Salom2ListCreateApiView.as_view()),
    path('3/',Salom3ListCreateApiView.as_view()),
    path('4/',Salom4ListCreateApiView.as_view()),
    path('5/',Salom5ListCreateApiView.as_view()),
 
]