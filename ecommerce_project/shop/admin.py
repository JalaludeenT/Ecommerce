from django.contrib import admin
from .models import Category, Product, Section


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Section)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'Section', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 50


admin.site.register(Product, ProductAdmin)
