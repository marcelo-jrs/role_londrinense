# Generated by Django 4.2.4 on 2023-09-14 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendario', '0008_alter_evento_local_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id_favorito', models.AutoField(primary_key=True, serialize=False)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.evento')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'favoritos',
            },
        ),
    ]
