# Generated by Django 5.0.2 on 2024-03-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_data',
            field=models.JSONField(default=dict),
        ),
    ]
