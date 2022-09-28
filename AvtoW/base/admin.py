from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'price', 'amount', 'manufacturer', 'contractor', 'brand', 'model', 'category')
    list_display_links = ('id', 'article', 'name')
    search_fields = ('id', 'article', 'name')
    list_filter = ('amount', 'manufacturer', 'contractor', 'brand', 'model', 'category')
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'inn', 'address', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'inn')


class ContractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'inn', 'address', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'inn')


class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'brand')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'phone', 'email')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_order')
    list_display_links = ('id', 'client')
    search_fields = ('client', 'date_order')


class Order_ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'amount')
    list_display_links = ('id', 'order', 'product')
    search_fields = ('id', 'order', 'product')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Item, Order_ItemAdmin)
