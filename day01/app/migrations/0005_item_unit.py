# Generated by Django 5.0.6 on 2024-07-31 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.unit'),
            preserve_default=False,
        ),
    ]
