# Generated by Django 5.1.1 on 2024-10-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_working',
            field=models.BooleanField(),
        ),
    ]