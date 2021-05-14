from django.db import models

# Create your models here.
class tb_products (models.Model):
    part_number= models.CharField(max_length=50)
    description= models.CharField(max_length=70)

class tb_cotizar(models.Model):
    name=models.CharField(max_length=70)
    mail=models.CharField(max_length=70)
    description=models.CharField(max_length=100)
