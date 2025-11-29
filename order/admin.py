from django.contrib import admin

from order.models import Order,Order_Detail

# Register your models here.
admin.site.register(Order)
admin.site.register(Order_Detail)
