# Generated by Django 3.2.11 on 2022-01-29 20:04

from django.db import migrations


def seed_menu_images(apps, schema_editor):
    images = [
        "3e1bd1342800f7",
        "23f95765b967ff",
        "70c2a6247e7b58",
        "95d02a230fe050",
        "5650be5d48a99b",
        "72589c4c990f97",
        "293202f9d9f7f4",
        "808916fd5ddf96",
        "b271afbefdc554",
        "bd237a0c0d19ef",
        "dba0fc03da30ca",
        "eba73b2361fae3",
        "f3fbf57b118fa9",
        "ffc9bf61e441cd",
    ]
    Image = apps.get_model("menu", "Image")
    for image in images:
        Image.objects.create(name=image, src=f"menu/{image}.jpg")


def clear_menu_images(apps, schema_editor):
    Image = apps.get_model("menu", "Image")
    for image in Image.objects.all():
        image.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_menu_images, reverse_code=clear_menu_images),
    ]
