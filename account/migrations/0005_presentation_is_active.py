# Generated by Django 2.0.2 on 2018-02-07 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_presentation_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]