from decimal import Decimal
from django.db import models

#Create your models here.
class shoppingPage(models.Model): 
    username = models.CharField(max_length=50, default='user')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=3)