# Generated by Django 2.2 on 2023-03-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctormodel',
            name='status',
            field=models.CharField(default='Free', max_length=30),
        ),
    ]
