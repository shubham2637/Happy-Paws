# Generated by Django 2.1.2 on 2018-11-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HappyPaws', '0011_dog_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='username',
            field=models.SlugField(max_length=128, unique=True),
        ),
    ]