from django.db import models


# Create your models here.
class Salom1(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="salom1/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Salom2(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="salom2/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Salom3(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="salom3/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Salom4(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="salom4/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Salom5(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="salom5/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)