# Generated by Django 4.2.2 on 2023-06-20 08:20

import accounts.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=accounts.fields.RandomField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
