from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from requests.api import delete

class Pessoa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=50)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    autor = models.CharField(max_length=50, default='Arnold')
    idioma = models.CharField(max_length=2, default='pt')

    def __str__(self):
        return f"{self.pk} | {self.user} | {self.telefone} | {self.altura} | {self.autor} | {self.idioma} "

    '''
    def __del__(self):
        Pessoa.delete(self.user)'''


class Peso(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=4, decimal_places=2)
    dataCadastro = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.pessoa} | {self.peso} | {self.imc} | {self.dataCadastro}"
