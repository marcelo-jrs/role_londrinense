# Generated by Django 4.2.4 on 2023-09-04 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0007_evento_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='local_online',
            field=models.CharField(choices=[('Local', 'Local'), ('Online', 'Online')], max_length=6),
        ),
    ]