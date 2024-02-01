# Generated by Django 3.2.23 on 2024-01-02 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Signup', '0002_alter_myuser_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('product_name', models.CharField(max_length=255)),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_desc', models.CharField(max_length=500)),
                ('min_bid_price', models.IntegerField()),
                ('product_img', models.ImageField(upload_to='products')),
                ('end_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Signup.myuser')),
            ],
        ),
    ]
