# Generated by Django 4.1.4 on 2022-12-22 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('band', models.TextField(max_length=100)),
                ('website', models.TextField(max_length=50)),
                ('bio', models.TextField(max_length=200)),
                ('photo_url', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistRig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guitar', models.TextField(max_length=200)),
                ('pedal1', models.TextField(max_length=100)),
                ('pedal2', models.TextField(max_length=100)),
                ('pedal3', models.TextField(max_length=100)),
                ('amplifier', models.TextField(max_length=100)),
                ('rig_year', models.TextField(max_length=200)),
                ('photo_url', models.TextField(max_length=500, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_rig', to='metal.artist')),
            ],
        ),
        migrations.CreateModel(
            name='RigDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=400)),
                ('tuning', models.TextField(max_length=200)),
                ('artistRig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rig_details', to='metal.artistrig')),
            ],
        ),
    ]
