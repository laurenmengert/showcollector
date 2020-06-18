# Generated by Django 3.0.7 on 2020-06-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('num_seasons', models.IntegerField()),
                ('description', models.TextField(max_length=300)),
                ('imdb_rating', models.IntegerField()),
            ],
        ),
    ]