from django.contrib import admin
from django.urls import path, include

app_name = 'YKG_Store'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
]
