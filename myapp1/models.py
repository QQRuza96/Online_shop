from django.db import models
    
class Product(models.Model):
    name = models.CharField(max_length=15, blank=False)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', default='product_images/default_image.jpg')
    
    def __str__(self):
        return f'{self.name}: {self.price} руб, {self.quantity} на складе id={self.id}'
