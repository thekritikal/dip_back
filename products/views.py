from django.shortcuts import render
from .serializer import CustomProductSerializer
from rest_framework import generics, permissions
from products.models import Product
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


# Create your views here.

def compare(size, colour, price1, price2, category, queryset):
    if category == None:
        if price1 == None and price2 == None:
            if size != None and colour != None:
                objects = queryset.filter(size=size, colour=colour).values()
                return Response(objects)
            if size == None and colour != None:
                objects = queryset.filter(colour=colour).values()
                return Response(objects)
            if size == None and colour == None:
                objects = queryset.all().values()
                return Response(objects)
            if size != None and colour == None:
                objects = queryset.filter(size=size).values()
                return Response(objects)
        else:
            if size != None and colour != None:
                objects = queryset.filter(size=size, colour=colour, price__gte=int(price1),price__lte=int(price2)).values()
                return Response(objects)
            if size == None and colour != None:
                objects = queryset.filter(colour=colour, price__gte=int(price1),price__lte=int(price2)).values()
                return Response(objects)
            if size == None and colour == None:
                objects = queryset.filter(price__gte=int(price1),price__lte=int(price2)).values()
                return Response(objects)
            if size != None and colour == None:
                objects = queryset.filter(size=size, price__gte=int(price1),price__lte=int(price2)).values()
                return Response(objects)
    else:
        if price1 == None and price2 == None:
            if size != None and colour != None:
                objects = queryset.filter(size=size, colour=colour, category=category).values()
                return Response(objects)
            if size == None and colour != None:
                objects = queryset.filter(colour=colour, category=category).values()
                return Response(objects)
            if size == None and colour == None:
                objects = queryset.filter(category=category).values()
                return Response(objects)
            if size != None and colour == None:
                objects = queryset.filter(size=size, category=category).values()
                return Response(objects)
        else:
            if size != None and colour != None:
                objects = queryset.filter(size=size, colour=colour, price__gte=int(price1),price__lte=int(price2), category=category).values()
                return Response(objects)
            if size == None and colour != None:
                objects = queryset.filter(colour=colour, price__gte=int(price1),price__lte=int(price2), category=category).values()
                return Response(objects)
            if size == None and colour == None:
                objects = queryset.filter(price__gte=int(price1),price__lte=int(price2), category=category).values()
                return Response(objects)
            if size != None and colour == None:
                objects = queryset.filter(size=size, price__gte=int(price1),price__lte=int(price2), category=category).values()
                return Response(objects)

class ProductList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomProductSerializer
    queryset = Product.objects.all()
    def get(self, request, **kwargs):
        size = request.GET.get("size")
        colour = request.GET.get("colour")
        price1 = request.GET.get("price1")
        price2 = request.GET.get("price2")
        category = request.GET.get("category")
        return compare(size, colour, price1, price2, category, self.queryset)


class GetManProducts(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomProductSerializer
    queryset = Product.objects.order_by('-id').filter(gender="man")
    def get(self, request, **kwargs):
        size = request.GET.get("size",)
        colour = request.GET.get("colour",)
        price1 = request.GET.get("price1",)
        price2 = request.GET.get("price2",)
        category = request.GET.get("category")
        return compare(size, colour, price1, price2, category, self.queryset)

class GetWomenProducts(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomProductSerializer
    queryset = Product.objects.order_by('-id').filter(gender="women")
    def get(self, request, **kwargs):
        size = request.GET.get("size",)
        colour = request.GET.get("colour",)
        price1 = request.GET.get("price1",)
        price2 = request.GET.get("price2",)
        category = request.GET.get("category")
        return compare(size, colour, price1, price2, category, self.queryset)

class GetShoesProducts(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomProductSerializer
    queryset = Product.objects.order_by('-id').filter(category="shoes")
    def get(self, request, **kwargs):
        size = request.GET.get("size",)
        colour = request.GET.get("colour",)
        price1 = request.GET.get("price1",)
        price2 = request.GET.get("price2",)
        category = request.GET.get("category")
        return compare(size, colour, price1, price2, category, self.queryset)


class GetClothingProducts(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomProductSerializer
    queryset = Product.objects.order_by('-id').filter(category="clothing")
    def get(self, request, **kwargs):
        size = request.GET.get("size",)
        colour = request.GET.get("colour",)
        price1 = request.GET.get("price1",)
        price2 = request.GET.get("price2",)
        category = request.GET.get("category")
        return compare(size, colour, price1, price2, category, self.queryset)

class GetAccessoriesProducts(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomProductSerializer
    queryset = Product.objects.order_by('-id').filter(category="accessories")
    def get(self, request, **kwargs):
        size = request.GET.get("size",)
        colour = request.GET.get("colour",)
        price1 = request.GET.get("price1",)
        price2 = request.GET.get("price2",)
        category = request.GET.get("category")
        return compare(size, colour, price1, price2, category, self.queryset)


class GetSaleProducts(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomProductSerializer
    queryset = Product.objects.order_by('-id').filter(sale=True)
    def get(self, request, **kwargs):
        size = request.GET.get("size",)
        colour = request.GET.get("colour",)
        price1 = request.GET.get("price1",)
        price2 = request.GET.get("price2",)
        category = request.GET.get("category")
        return compare(size, colour, price1, price2, category, self.queryset)

class ProductDetail(generics.RetrieveAPIView):
    serializer_class = CustomProductSerializer
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Product, id=item)
