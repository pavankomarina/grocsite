# Generated by Django 4.0.2 on 2022-02-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
