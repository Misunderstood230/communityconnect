# Generated by Django 5.1.7 on 2025-03-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com', '0018_adminrequest_approved_volunteers'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
