# Generated by Django 5.0.2 on 2024-02-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Samsung', 'Samsung'), ('Vivo', 'Vivo'), ('Nubia', 'Nubia'), ('IQoo', 'IQoo'), ('Apple', 'Apple'), ('Xiaomi', 'Xiaomi'), ('Redmi', 'Redmi'), ('Oppo', 'Oppo'), ('Realme', 'Realme'), ('Honor', 'Honor')], max_length=100),
        ),
    ]