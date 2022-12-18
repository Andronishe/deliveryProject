from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

@admin.register(Courier)
class CourierAdmin(ModelAdmin):
    list_display = ('id', 'name', 'telephone', 'delivery_type')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name',)



admin.site.register(Order)
# admin.site.register(Product)
# admin.site.register(Courier)
admin.site.register(DeliveryList)
admin.site.register(OrdersProducts)
# admin.site.register(User)