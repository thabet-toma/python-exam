# Generated by Django 2.2.4 on 2022-10-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_trees'),
    ]

    operations = [
        migrations.AddField(
            model_name='trees',
            name='visitors',
            field=models.ManyToManyField(null=True, related_name='user_visitors', to='app.Users'),
        ),
    ]
