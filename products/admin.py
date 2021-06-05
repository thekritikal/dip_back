from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    list_display=('id', 'name', 'brand', 'description', 'price', 'sale', 'gender', 'category', 'size', 'colour', 'image1', 'image2', 'image3', 'image4', 'composition1', 'composition2', 'composition3', 'designer_article',)
