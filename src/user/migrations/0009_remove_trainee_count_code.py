# Generated by Django 2.2.10 on 2020-04-05 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_trainer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='count_code',
        ),
    ]
