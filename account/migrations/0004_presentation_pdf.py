# Generated by Django 2.0.2 on 2018-02-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180207_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='pdf',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
