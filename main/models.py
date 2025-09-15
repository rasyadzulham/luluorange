import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('atasan', 'Atasan'),
        ('bawahan', 'Bawahan'),
        ('sepatu', 'Sepatu'),
        ('aksesoris', 'Aksesoris'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_recommended(self):
        return self.rating > 4