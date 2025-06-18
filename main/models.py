from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    price = models.IntegerField()
    

    def __str__(self):
        return self.name