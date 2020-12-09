from django.db import models


class Marque(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField()
    supplier_info = models.TextField(null=True)


class Type(models.Model):
    name = models.CharField(max_length=200, unique=True)
    img_url = models.URLField()
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE, null=True)


class Department (models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.TextField(null=True)
    info = models.TextField(null=True)


class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    model = models.CharField(max_length=200, unique=True)
    note_info = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)


