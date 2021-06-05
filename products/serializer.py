from rest_framework import serializers
from products.models import Product

class CustomProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=(
            'id',
            'name',
            'brand',
            'description',
            'price',
            'sale',
            'gender',
            'category',
            'size',
            'colour',
            'image1',
            'image2',
            'image3',
            'image4',
            'composition1',
            'composition2',
            'composition3',
            'designer_article',

        )
