from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False)
    product_info = models.TextField()
    price = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True) 
    seller = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField()
    post = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


