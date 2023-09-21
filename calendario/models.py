from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nome_evento = models.TextField()
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    local_online = models.CharField(choices=[("Local", "Local"),("Online", "Online")], max_length=6)
    faixa_etaria = models.IntegerField()
    endereco = models.TextField(blank=True)
    website = models.TextField()
    politica = models.TextField()
    banner = models.ImageField(null=True, blank=True, upload_to="images/")
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "eventos"

class Favoritos(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "favoritos"

