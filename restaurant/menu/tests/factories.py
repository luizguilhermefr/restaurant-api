from uuid import uuid4

import factory

from restaurant.menu.models import Image, Category, MenuItem


class ImageFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: uuid4())

    class Meta:
        model = Image


class CategoryFactory(factory.DjangoModelFactory):
    image = factory.RelatedFactory(ImageFactory)

    class Meta:
        model = Category


class MenuItemFactory(factory.DjangoModelFactory):
    category = factory.RelatedFactory(CategoryFactory)
    image = factory.RelatedFactory(ImageFactory)
    price = 25

    class Meta:
        model = MenuItem
