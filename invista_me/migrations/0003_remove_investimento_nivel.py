# Generated by Django 5.0.1 on 2024-02-13 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0002_investimento_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='nivel',
        ),
    ]