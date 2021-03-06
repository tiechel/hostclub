# Generated by Django 3.1.2 on 2020-10-22 18:54

from django.db import migrations, models
import django.db.models.deletion
import hostclub.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='お客様名')),
                ('image', models.ImageField(blank=True, upload_to=hostclub.models.get_image_path, verbose_name='画像')),
                ('memo', models.TextField(blank=True, default='', verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': 'お客様',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ホスト名')),
            ],
            options={
                'verbose_name_plural': 'ホスト',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('price', models.BigIntegerField(verbose_name='価格')),
                ('tax_rate', models.FloatField(choices=[('10', '10%'), ('8', '8%（軽減税率）'), ('0', '0%(非課税)')], default='10')),
            ],
            options={
                'verbose_name_plural': 'メニュー',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='シート名')),
            ],
            options={
                'verbose_name_plural': 'シート',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entered_at', models.DateTimeField(verbose_name='入店日時')),
                ('left_at', models.DateTimeField(verbose_name='退店日時')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reserves', to='hostclub.customer')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reserves', to='hostclub.host')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reserves', to='hostclub.seat')),
            ],
            options={
                'verbose_name_plural': '予約',
            },
        ),
    ]
