# Generated by Django 2.2.11 on 2021-03-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210315_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
