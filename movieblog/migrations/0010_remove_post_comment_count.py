# Generated by Django 3.1.4 on 2021-06-25 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieblog', '0009_auto_20210625_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]