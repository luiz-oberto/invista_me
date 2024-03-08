from django.db import models
from datetime import datetime
'''
* investimento
* valor
* pago
* data

documentação de models django
https://docs.djangoproject.com/en/4.2/topics/db/models/?_gl=1*xbgvvn*_ga*NjI2NDY0Mzg2LjE3MDQzMDMwNzA.*_ga_37GXT4VGQK*MTcwNzg0Nzg2Ny4zNy4xLjE3MDc4NDc5OTMuMC4wLjA.

'''
class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
