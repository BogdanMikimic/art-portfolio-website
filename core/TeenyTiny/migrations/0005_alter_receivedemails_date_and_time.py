# Generated by Django 3.2.8 on 2021-11-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeenyTiny', '0004_receivedemails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receivedemails',
            name='date_and_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
