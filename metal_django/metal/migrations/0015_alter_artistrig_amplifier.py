# Generated by Django 4.1.4 on 2022-12-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metal', '0014_artistrig_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistrig',
            name='amplifier',
            field=models.TextField(max_length=400),
        ),
    ]
