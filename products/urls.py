from django.urls import path
from .views import ProductList, GetManProducts, GetWomenProducts, GetShoesProducts, GetClothingProducts, GetAccessoriesProducts, ProductDetail, GetSaleProducts

app_name = 'Products'

urlpatterns = [
    path('', ProductList.as_view(), name='ProductList'),
    path('man/', GetManProducts.as_view(), name='manProductList'),
    path('women/', GetWomenProducts.as_view(), name='womenProductList'),
    path('sale/', GetSaleProducts.as_view(), name='saleProductList'),
    path('shoes/', GetShoesProducts.as_view(), name='shoesProductList'),
    path('clothing/', GetClothingProducts.as_view(), name='clothingProductList'),
    path('accessories/', GetAccessoriesProducts.as_view(), name='accessoriesProductList'),
    path('<str:pk>/', ProductDetail.as_view(), name='detailproducts'),


]
