# Generated by Django 3.0.6 on 2020-05-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
