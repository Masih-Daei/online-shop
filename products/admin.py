from django.contrib import admin
from .models import Products ,ProductGallery

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active','featured','visits']

    class Meta:
        model = Products


# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(ProductGallery)