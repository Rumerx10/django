# Generated by Django 3.2.23 on 2024-01-03 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_productdetails_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='product_img',
            field=models.ImageField(max_length=255, upload_to='productsImg/'),
        ),
    ]