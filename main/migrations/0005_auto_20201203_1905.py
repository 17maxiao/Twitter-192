# Generated by Django 3.1.4 on 2020-12-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201203_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlikes',
            name='number',
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='tweet',
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='users',
        ),
        migrations.AddField(
            model_name='tweet',
            name='userlikes',
            field=models.ManyToManyField(to='main.UserLikes'),
        ),
        migrations.AddField(
            model_name='userlikes',
            name='user',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
