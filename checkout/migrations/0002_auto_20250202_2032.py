# Generated by Django 3.2.25 on 2025-02-02 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='strip_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
