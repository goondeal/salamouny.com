# Generated by Django 3.2.4 on 2021-06-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
