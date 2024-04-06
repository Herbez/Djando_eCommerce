from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	email = models.EmailField(max_length=100)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=100)


	def __str__(self):
		return f'{self.username}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.IntegerField()
    description=models.CharField(max_length=100)

