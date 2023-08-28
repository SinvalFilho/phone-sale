from django.db import models
from django.contrib.auth.models import User
from products.models import Celular

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    celular = models.ForeignKey(Celular, on_delete=models.CASCADE, related_name='avaliacoes')
    comentario = models.TextField()
    pontuacao = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.celular.marca} {self.celular.modelo} por {self.usuario.username}"
