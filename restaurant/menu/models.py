from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image_id = models.CharField(max_length=255)


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    image_id = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
