from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nome_evento = models.TextField()
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    local_online = models.IntegerField()
    faixa_etaria = models.IntegerField()
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "eventos"