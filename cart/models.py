from django.db import models
from inventory.models import Products
from order .models import Order

# Create your models here.
class Cart(models.Model):
    inventory=models.ManyToManyField(Products)
    order=models.ForeignKey(Order,on_delete=models.CASCADE )
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    total_amount=models.PositiveBigIntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)


 # quantity=models.PositiveBigIntegerField()
    # shipping_cost=models.DecimalField(max_digits=6,decimal_places=2)
    # payment_options=models.CharField(max_length=32)

def __str__(self):
    return self.name