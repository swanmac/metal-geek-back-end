# Generated by Django 4.1.4 on 2022-12-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metal', '0012_artistrig_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistrig',
            name='name',
        ),
    ]
