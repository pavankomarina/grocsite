# Generated by Django 4.0.2 on 2022-02-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_remove_client_fullname_client_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
