# Generated by Django 5.1.3 on 2025-01-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('png', '0009_alter_event_event_date_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
