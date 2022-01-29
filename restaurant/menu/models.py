from django.db import models


class Image(models.Model):
    src = models.ImageField(upload_to="menu/")
    name = models.CharField(unique=True, max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
