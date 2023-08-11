from django.db import models
from payment.models import Payment
from inventory.models import Products
from customer.models import Customer
from cart.models import Cart 

# Create your models here.
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,null=True)
    # shipment=models.ForeignKey(Shipment,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=32)
    customer_name=models.CharField(max_length=32)
    items=models.CharField(max_length=32)
    discount_percentage=float()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
def __str__(self):
    return self.name
# return f"order #{self.pk}