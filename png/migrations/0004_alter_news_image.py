# Generated by Django 5.1.3 on 2025-01-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('png', '0003_event_news_alter_reg_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news_img'),
        ),
    ]
