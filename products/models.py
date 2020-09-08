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
    like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through='Like')

    @property
    def like_count(self):
        return self.like_user_set.count()
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='comments')
    writer = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'product'))

