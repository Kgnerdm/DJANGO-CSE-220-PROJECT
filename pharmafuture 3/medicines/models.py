from django.db import models

class Medicine(models.Model):
    CATEGORIES = [
        ('Antibiotic', 'Antibiotic'),
        ('Anti-Allergic', 'Anti-Allergic'),
        ('Antidepressant', 'Antidepressant'),
        ('Painkiller', 'Painkiller'),
        ('Vitamins', 'Vitamins'),
    ]

    name = models.CharField(max_length=100, default='Unknown Medicine')
    description = models.TextField()
    photo = models.ImageField(upload_to='img', default='medicines/static/img/1.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='Vitamins')  # Add category field
    
    
    def __str__(self):
        return self.name
    
class HomeProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='img')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
