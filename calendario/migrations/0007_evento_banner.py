# Generated by Django 4.2.4 on 2023-09-04 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0006_evento_endereco_evento_politica_evento_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
