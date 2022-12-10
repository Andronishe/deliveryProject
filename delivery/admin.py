from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Courier)
admin.site.register(DeliveryList)
admin.site.register(OrdersProducts)
admin.site.register(Customer)