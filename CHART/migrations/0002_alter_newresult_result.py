# Generated by Django 5.0.2 on 2024-09-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CHART', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newresult',
            name='result',
            field=models.CharField(max_length=2),
        ),
    ]
