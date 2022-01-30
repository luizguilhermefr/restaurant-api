from uuid import uuid4

import factory

from restaurant.menu.models import Image, Category, MenuItem, Order, Payment, OrderItem


class ImageFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: uuid4())

    class Meta:
        model = Image


class CategoryFactory(factory.django.DjangoModelFactory):
    image = factory.SubFactory(ImageFactory)

    class Meta:
        model = Category


class MenuItemFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    image = factory.SubFactory(ImageFactory)
    price = 25

    class Meta:
        model = MenuItem


class PaymentFactory(factory.django.DjangoModelFactory):
    confirmation = factory.LazyAttribute(lambda x: uuid4())

    class Meta:
        model = Payment


class OrderFactory(factory.django.DjangoModelFactory):
    payment = factory.SubFactory(PaymentFactory)

    class Meta:
        model = Order


class OrderItemFactory(factory.django.DjangoModelFactory):
    item = factory.SubFactory(MenuItemFactory)
    order = factory.SubFactory(OrderFactory)
    quantity = 1
    price = 25

    class Meta:
        model = OrderItem
