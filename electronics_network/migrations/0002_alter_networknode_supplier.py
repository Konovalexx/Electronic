# Generated by Django 5.1.3 on 2024-12-09 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electronics_network", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="networknode",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clients",
                to="electronics_network.networknode",
            ),
        ),
    ]
