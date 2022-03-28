# Generated by Django 4.0.3 on 2022-03-28 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('phone_code', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=200)),
                ('firstname', models.CharField(default='', max_length=200)),
                ('middlename', models.CharField(default='', max_length=200)),
                ('lastname', models.CharField(default='', max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('avatar', models.CharField(default='/static/index/img/img_avatar.png', max_length=60)),
                ('full_phone_num', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(max_length=6)),
                ('document', models.CharField(max_length=60)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.customer')),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=100, unique=True)),
                ('public_key', models.CharField(max_length=100, unique=True)),
                ('private_key', models.CharField(max_length=100, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.customer')),
            ],
        ),
    ]
