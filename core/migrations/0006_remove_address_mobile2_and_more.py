# Generated by Django 4.2.3 on 2023-12-31 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_contact_vendor_contact1_vendor_contact2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='mobile2',
        ),
        migrations.AlterField(
            model_name='residenceimages',
            name='Residence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='R_images', to='core.residence'),
        ),
    ]