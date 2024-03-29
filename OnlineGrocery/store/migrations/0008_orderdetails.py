# Generated by Django 4.2.9 on 2024-03-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=True)),
                ('product_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('price', models.IntegerField()),
                ('orderd_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=50)),
            ],
        ),
    ]
