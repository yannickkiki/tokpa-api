# Generated by Django 2.2.11 on 2021-03-15 14:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
