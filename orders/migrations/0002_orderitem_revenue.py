# Generated by Django 5.0.1 on 2024-01-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="revenue",
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
    ]