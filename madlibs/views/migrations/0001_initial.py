# Generated by Django 2.2 on 2020-11-28 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun', models.CharField(max_length=100)),
                ('adjective', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('expression', models.CharField(max_length=100)),
            ],
        ),
    ]