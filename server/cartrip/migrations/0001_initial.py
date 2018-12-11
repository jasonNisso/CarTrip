# Generated by Django 2.1.4 on 2018-12-11 20:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('date', models.DateTimeField(verbose_name='BundleDates')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=0, verbose_name='year')),
                ('color', models.CharField(max_length=200)),
                ('extra_information', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2018, 12, 11, 22, 56, 13, 665277))),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('engine_cubic_centimeters', models.CharField(max_length=20)),
                ('engine_manufacturer', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('date', models.DateTimeField(verbose_name='excursionDate')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('cars', models.ManyToManyField(to='cartrip.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('date', models.DateTimeField(verbose_name='exhibitionDate')),
                ('description', models.TextField(blank=True, max_length=800, null=True)),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('cars', models.ManyToManyField(to='cartrip.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_address', models.CharField(max_length=200)),
                ('map_location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='Post')),
                ('post_date', models.DateTimeField(default=datetime.datetime(2018, 12, 11, 22, 56, 13, 664872))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=0, verbose_name='userType')),
                ('username', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('bundles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartrip.Bundle')),
                ('excursions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartrip.Excursion')),
                ('exhibitions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartrip.Exhibition')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartrip.User'),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='location',
            field=models.ManyToManyField(to='cartrip.Location'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='location',
            field=models.ManyToManyField(to='cartrip.Location'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartrip.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartrip.Post'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartrip.Engine'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='excursion',
            field=models.ManyToManyField(to='cartrip.Excursion'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='exhibitions',
            field=models.ManyToManyField(to='cartrip.Exhibition'),
        ),
    ]
