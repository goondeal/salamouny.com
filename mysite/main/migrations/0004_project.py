# Generated by Django 3.2.4 on 2021-07-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, null=True)),
                ('src_code_url', models.URLField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]