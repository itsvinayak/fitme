# Generated by Django 3.0.4 on 2020-03-31 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200328_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traineephy',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='phone',
        ),
        migrations.AddField(
            model_name='trainee',
            name='image',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='TraineeAddress',
        ),
        migrations.DeleteModel(
            name='TraineePhy',
        ),
    ]
