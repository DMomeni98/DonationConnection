from django.contrib import admin
from .models import Product
from products.forms import ProductForm
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)