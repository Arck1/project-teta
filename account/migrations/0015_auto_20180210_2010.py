# Generated by Django 2.0.2 on 2018-02-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_presentation_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='stat',
            field=models.TextField(blank=True, default='[]', null=True),
        ),
    ]
