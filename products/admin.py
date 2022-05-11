from django.contrib import admin
from .models import Category, Habitat, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')

@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name', 'water_need', 'light_need')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name', 'category', 'price', 'size', 'habitat')
