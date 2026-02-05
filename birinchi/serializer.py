from rest_framework.serializers import ModelSerializer
from birinchi.models import Salom1, Salom2, Salom3, Salom4, Salom5


class Salom1Serializer(ModelSerializer):

    class Meta:
        model = Salom1
        fields = "__all__"


class Salom2Serializer(ModelSerializer):

    class Meta:
        model = Salom2
        fields = "__all__"


class Salom3Serializer(ModelSerializer):

    class Meta:
        model = Salom3
        fields = "__all__"


class Salom4Serializer(ModelSerializer):

    class Meta:
        model = Salom4
        fields = "__all__"


class Salom5Serializer(ModelSerializer):

    class Meta:
        model = Salom5
        fields = "__all__"