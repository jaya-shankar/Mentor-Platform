# Generated by Django 3.0.2 on 2020-06-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorPage', '0008_auto_20200613_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='time',
            field=models.DateTimeField(),
        ),
    ]