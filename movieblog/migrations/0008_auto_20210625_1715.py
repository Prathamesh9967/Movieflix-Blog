# Generated by Django 3.1.4 on 2021-06-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieblog', '0007_auto_20210625_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='PostView',
        ),
    ]