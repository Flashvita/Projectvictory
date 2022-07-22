from django.contrib import admin
from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Customer, CustomerAdmin)
