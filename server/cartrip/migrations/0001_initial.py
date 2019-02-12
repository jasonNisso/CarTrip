# Generated by Django 2.1.4 on 2019-02-12 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('extra_information', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(default='Comment')),
                ('comment_date', models.DateTimeField(auto_now=True)),
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
                ('description', models.TextField(blank=True, max_length=800, null=True)),
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
                ('title', models.TextField(default='Title')),
                ('text', models.TextField(default='Post')),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
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
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartrip.Post'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cartrip.Engine'),
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bundle',
            name='excursions',
            field=models.ManyToManyField(to='cartrip.Excursion'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='exhibitions',
            field=models.ManyToManyField(to='cartrip.Exhibition'),
        ),
    ]