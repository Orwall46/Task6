# Generated by Django 4.1.3 on 2022-11-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='procent',
            field=models.PositiveIntegerField(verbose_name='Procent_discount'),
        ),
    ]