# Generated by Django 4.0.2 on 2022-03-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0004_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client'},
        ),
        migrations.AddField(
            model_name='item',
            name='interested',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
