# Generated by Django 4.2 on 2024-09-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cost',
            field=models.BigIntegerField(default=0),
        ),
    ]
