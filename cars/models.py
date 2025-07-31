from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)                     # identificador unico do registro do carro na tabela
    model = models.CharField(max_length=200)                    # modelo do carro
    brand = models.CharField(max_length=200)                    # marca
    factory_year = models.IntegerField(blank=True, null=True)   # ano de fabricacao
    model_year = models.IntegerField(blank=True, null=True)     # ano do modelo
    value = models.FloatField(blank=True, null=True)            # valor do carro