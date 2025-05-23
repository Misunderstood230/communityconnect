# Generated by Django 5.1 on 2025-03-05 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com', '0002_request_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accept_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', ' Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='com.request')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='com.reg')),
            ],
        ),
    ]
