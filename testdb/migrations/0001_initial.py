# Generated by Django 4.1.1 on 2022-09-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=500)),
                ('Name', models.CharField(max_length=500)),
                ('Email', models.CharField(max_length=100)),
                ('Bio', models.CharField(max_length=300)),
                ('Repos', models.IntegerField(max_length=200)),
            ],
        ),
    ]
