# Generated by Django 5.0.2 on 2024-02-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
