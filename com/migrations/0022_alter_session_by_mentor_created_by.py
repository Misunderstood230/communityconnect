# Generated by Django 5.1.7 on 2025-03-28 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com', '0021_session_by_mentor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_by_mentor',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_sessions', to='com.mod'),
        ),
    ]
