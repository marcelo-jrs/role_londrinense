# Generated by Django 4.2.4 on 2023-09-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0009_favoritos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='endereco',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='politica',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='website',
            field=models.TextField(),
        ),
    ]
