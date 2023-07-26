from django.db import models

# Create your models here.
class Payment(models.Model):
    date=models.DateTimeField()
    balance=models.FloatField(max_length=8)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    def __date__(self):
        return self.date
