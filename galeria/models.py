from django.db import models
from django.contrib.auth.models import User
# Create your models here.
OPCOES_CATEGORIA = (
    ("NEBULOSA", "Nebulosa"),
    ("ESTRELA", "Estrela"),
    ("GALÁXIA", "Galáxia"),
    ("PLANETA", "Planeta"),
)


class Fotografia(models.Model):
    nome = models.CharField(max_length=250, null=False, blank=False)
    legenda = models.CharField(max_length=250, null=False, blank=False)
    categoria = models.CharField(max_length=250, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user")
    horaCadastro = models.DateTimeField(u'Data e Hora', auto_now=True)

    def __str__(self) -> str:
        return self.nome
