# Generated by Django 4.1.4 on 2022-12-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metal', '0011_alter_rigdetail_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistrig',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]