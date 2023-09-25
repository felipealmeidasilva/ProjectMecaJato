from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.nome
    
class Carro(models.Model):
    carro = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.carro   