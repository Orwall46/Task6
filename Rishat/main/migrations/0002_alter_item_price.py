# Generated by Django 4.1.3 on 2022-11-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Price'),
        ),
    ]
