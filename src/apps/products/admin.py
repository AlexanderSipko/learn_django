
from django.contrib import admin
from .models import Product, Order



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "description", 'quantity', 'price')
    list_filter = ("price", )
    search_fields = ("title", )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass