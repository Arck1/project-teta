# Generated by Django 2.0.2 on 2018-02-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_presentation_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='stat',
            field=models.TextField(blank=True, default='{}', null=True),
        ),
    ]
