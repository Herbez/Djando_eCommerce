from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.IntegerField()
    description=models.CharField(max_length=100)