# Generated by Django 3.0.1 on 2021-01-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_brand_side_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='key_features',
            field=models.TextField(null=True),
        ),
    ]
