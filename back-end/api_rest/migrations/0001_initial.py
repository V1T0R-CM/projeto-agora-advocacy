# Generated by Django 5.0.4 on 2024-04-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propositions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=24, unique=True)),
                ('url', models.URLField(default='', unique=True)),
                ('keyWords', models.TextField(default='')),
            ],
        ),
    ]
