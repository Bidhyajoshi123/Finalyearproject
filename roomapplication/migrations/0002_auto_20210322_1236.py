# Generated by Django 3.1.7 on 2021-03-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]