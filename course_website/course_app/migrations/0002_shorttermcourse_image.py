# Generated by Django 3.2.5 on 2023-06-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorttermcourse',
            name='image',
            field=models.ImageField(default=False, upload_to='course_images/'),
        ),
    ]
