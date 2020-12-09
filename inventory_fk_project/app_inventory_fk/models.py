from django.db import models


class Marque(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField()
    logo_img_url = models.URLField()
    optional_info = models.TextField(null=True)


class Type(models.Model):
    name = models.CharField(max_length=200, unique=True)


class ModelItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    img_url = models.URLField()
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE, null=True)
    optional_info = models.TextField(null=True)


class Department (models.Model):
    name = models.CharField(max_length=200, unique=True)
    optional_info = models.TextField(null=True)


class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    model = models.CharField(max_length=200, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    optional_info = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


