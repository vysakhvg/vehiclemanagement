# Generated by Django 4.2.3 on 2023-07-13 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=250)),
                ('vehicle_type', models.CharField(max_length=250)),
                ('vehicle_model', models.CharField(max_length=250)),
                ('vehicle_description', models.TextField()),
            ],
        ),
    ]
