# Generated by Django 3.1 on 2020-08-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='answer',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=6),
        ),
    ]