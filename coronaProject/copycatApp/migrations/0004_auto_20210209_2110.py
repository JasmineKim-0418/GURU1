# Generated by Django 3.1.6 on 2021-02-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copycatApp', '0003_news_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='day',
            field=models.CharField(max_length=50),
        ),
    ]