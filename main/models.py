from django.db import models

# Create your models here.

# category_choices = [
#     ("electronics", "Electronics"),
#     ("fashion", "Fashion"),
#     ("home", "Home"),
#     ("books", "Books"),
#     ("toys", "Toys"),
#     ("sports", "Sports"),
#     ("beauty", "Beauty"),
#     ("automotive", "Automotive"),
#     ("grocery", "Grocery"),
#     ("health", "Health"),
# ]

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    #category = models.CharField(max_length=20, choices=category_choices, default="electronics")
   #tags = models.CharField(max_length=100, blank=True)  # Comma-separated tags
    price = models.DecimalField(max_digits=10, decimal_places=2)
   # new_since = models.DateTimeField(auto_now_add=True)


    # def is_new(self):
    #     from django.utils import timezone
    #     return (timezone.now() - self.new_since).days < 30

    

    def __str__(self):
        return self.name
    
#TODO: Add category and tags fields to Product model and implement filtering based on them in views.    