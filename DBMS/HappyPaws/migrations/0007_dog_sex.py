# Generated by Django 2.1.2 on 2018-11-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HappyPaws', '0006_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='sex',
            field=models.CharField(default='male', max_length=8),
            preserve_default=False,
        ),
    ]
