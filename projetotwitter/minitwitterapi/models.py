from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class Postagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    texto_da_postagem = models.TextField(max_length=256)


    def __str__(self) -> str:
        return f'id: {self.id} - título: {self.titulo}'