# Generated by Django 4.0.5 on 2022-06-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='Duration',
            field=models.IntegerField(),
        ),
    ]
