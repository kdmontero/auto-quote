# Generated by Django 5.1.7 on 2025-04-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
    ]
