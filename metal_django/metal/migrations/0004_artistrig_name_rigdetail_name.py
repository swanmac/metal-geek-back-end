# Generated by Django 4.1.4 on 2022-12-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metal', '0003_alter_artist_bio_alter_artist_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistrig',
            name='name',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rigdetail',
            name='name',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
