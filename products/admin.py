from django.contrib import admin
from .models import Product, Review

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "product_info",
        "price",
        "stock",
        "image",
        "created_at",
        "updated_at",
        "seller",
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "rating",
        "post",
        "created_at",
        "updated_at",
    )