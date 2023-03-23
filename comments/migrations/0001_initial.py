# Generated by Django 4.1.7 on 2023-03-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city', models.CharField(default='none', max_length=15)),
                ('rating', models.IntegerField(default=1)),
                ('review', models.CharField(max_length=300)),
            ],
        ),
    ]
