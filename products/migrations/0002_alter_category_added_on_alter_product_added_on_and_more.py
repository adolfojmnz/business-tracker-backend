# Generated by Django 5.0.1 on 2024-01-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="added_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="added_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="unit",
            name="added_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]