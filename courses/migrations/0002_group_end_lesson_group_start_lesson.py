# Generated by Django 4.1.4 on 2022-12-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='end_lesson',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='start_lesson',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
