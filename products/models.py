from django.db import models
from datetime import datetime

class Celular(models.Model):
    MARCAS_CHOICES = [
        ('Apple', 'Apple'),
        ('Samsung', 'Samsung'),
        ('Xiaomi', 'Xiaomi'),
        ('Huawei', 'Huawei'),
        ('Motorola', 'Motorola'),
        ('OnePlus', 'OnePlus'),
    ]

    marca = models.CharField(max_length=100, choices=MARCAS_CHOICES, blank=False)
    modelo = models.CharField(max_length=100, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    estoque = models.PositiveIntegerField()
    publicada = models.BooleanField(default=False)
    data_atualizacao = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return f"Celular [nome= {self.marca}]"
