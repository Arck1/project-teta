# Generated by Django 2.0.2 on 2018-02-10 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20180210_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='pdf',
            field=models.FileField(blank=True, default=None, null=True, upload_to='user_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
