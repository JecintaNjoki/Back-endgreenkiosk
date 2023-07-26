from django.db import models
from inventory.models import Products

# Create your models here.
class Cart(models.Model):
    inventory=models.ManyToManyField(Products) 
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    total_amount=models.PositiveBigIntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name