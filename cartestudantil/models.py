from django.db import models

class CarteiraEstudante(models.Model):
    nome_completo = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='fotos_carteiras/')
    validade = models.DateField()

    def __str__(self):
        return f"{self.nome_completo} - {self.matricula}"