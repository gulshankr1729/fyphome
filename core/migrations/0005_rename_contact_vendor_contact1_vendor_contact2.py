# Generated by Django 4.2.3 on 2023-12-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_mobile_address_mobile1_address_mobile2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='contact',
            new_name='contact1',
        ),
        migrations.AddField(
            model_name='vendor',
            name='contact2',
            field=models.CharField(default='+123 (456) 789', max_length=100),
        ),
    ]
