# Generated by Django 4.2.5 on 2023-09-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='single_picture',
            name='caption',
            field=models.TextField(blank=True, default='Add a cute message!', null=True),
        ),
    ]