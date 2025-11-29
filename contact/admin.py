from django.contrib import admin

from .models import contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'email', 'read']

    class Meta:
        model = contact


# Register your models here.
admin.site.register(contact,ContactAdmin)