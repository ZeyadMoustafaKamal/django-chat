# Generated by Django 4.1.9 on 2023-06-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]