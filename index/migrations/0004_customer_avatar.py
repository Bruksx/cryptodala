# Generated by Django 3.2 on 2022-03-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20220228_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.CharField(default='/static/index/img/img_avatar.png', max_length=60),
        ),
    ]
