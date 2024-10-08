# Generated by Django 5.1 on 2024-09-17 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='client_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Адрес не указан', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='Почта не указан', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='Телефон не указан', max_length=15),
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='review_images/'),
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.author'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service'),
        ),
    ]
