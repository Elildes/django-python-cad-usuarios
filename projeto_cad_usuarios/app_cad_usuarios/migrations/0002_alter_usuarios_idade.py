# Generated by Django 5.0.3 on 2024-03-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
