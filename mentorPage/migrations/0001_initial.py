# Generated by Django 3.0.2 on 2020-05-29 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=20)),
                ('description', models.CharField(max_length=150)),
                ('takeaways', models.CharField(max_length=200)),
                ('creator', models.IntegerField(null=True)),
            ],
        ),
    ]
