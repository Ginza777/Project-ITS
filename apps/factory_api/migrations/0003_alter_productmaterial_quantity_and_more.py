# Generated by Django 5.0.3 on 2024-03-15 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory_api', '0002_warehouse_for_check_remainder_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmaterial',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='for_check_remainder_count',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='remainder',
            field=models.FloatField(),
        ),
    ]
