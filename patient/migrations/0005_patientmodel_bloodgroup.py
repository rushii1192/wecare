# Generated by Django 2.2 on 2023-03-18 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20230318_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmodel',
            name='bloodGroup',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]