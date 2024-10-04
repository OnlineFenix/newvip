# Generated by Django 5.0.2 on 2024-09-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CHART', '0002_alter_newresult_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
