# Generated by Django 4.1.3 on 2022-11-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Descriptions')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price')),
            ],
        ),
    ]
