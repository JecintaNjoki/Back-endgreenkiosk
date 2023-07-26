from django.db import models

# Create your models here.
class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

def __str__(self):
    return self.review