from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField()
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return self.nome