from django.db import models

# Create your models here.


class Product(models.Model):
    optionsGender = (
        ('man', 'Man'),
        ('women', 'Women'),
    )
    optionsCategory = (
        ('clothing', 'Clothing'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
    )
    name=models.CharField(max_length=244)
    brand=models.CharField(max_length=244)
    description=models.CharField(max_length=500)
    price=models.PositiveIntegerField(blank=False)
    sale=models.BooleanField(blank=False)
    gender=models.CharField(max_length=244, default='man', choices=optionsGender)
    category=models.CharField(max_length=244, default='clothing', choices=optionsCategory)
    size=models.CharField(max_length=244, default = None, blank=True, null=True)
    colour=models.CharField(max_length=244, default = None, blank=True, null=True)
    image1 = models.URLField(default = "https://image.emojipng.com/883/13277883.jpg")
    image2 = models.URLField(default = "https://image.emojipng.com/883/13277883.jpg")
    image3 = models.URLField(default = "https://image.emojipng.com/883/13277883.jpg")
    image4 = models.URLField(default = "https://image.emojipng.com/883/13277883.jpg")
    composition1 = models.CharField(max_length=244, default = None, blank=True, null=True)
    composition2 = models.CharField(max_length=244, default = None, blank=True, null=True)
    composition3 = models.CharField(max_length=244, default = None, blank=True, null=True)
    designer_article = models.CharField(max_length=244, default = None, blank=True, null=True)
