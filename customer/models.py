from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    password=models.CharField(max_length=12)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
def __str__(self):
    return self.first_name