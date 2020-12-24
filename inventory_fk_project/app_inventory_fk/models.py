from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField()
    logo_img_url = models.URLField()
    optional_info = models.TextField(null=True)

    def delete_brand(self):
        pass


class Type(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def delete_type(self):
        pass


class ModelItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    img_url = models.URLField()
    marque = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    optional_info = models.TextField(null=True)

    def delete_modelItem(self):
        pass


class Department (models.Model):
    name = models.CharField(max_length=200, unique=True)
    optional_info = models.TextField(null=True)

    def delete_departement(self):
        pass


class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    model = models.CharField(max_length=200, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    serial_number = models.CharField(max_length=200, unique=True, null=True)
    optional_info = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete_item(self):
        pass


