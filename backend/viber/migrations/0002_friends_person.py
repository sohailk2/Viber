# Generated by Django 3.1.2 on 2020-11-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendFrom', models.TextField(blank=True, null=True)),
                ('friendTo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'friend',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.TextField(blank=True, null=True)),
                ('spotifyID', models.TextField(blank=True, null=True)),
                ('favoriteSong', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]