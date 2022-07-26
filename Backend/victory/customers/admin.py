from django.contrib import admin
from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'id','email')


admin.site.register(Customer, CustomerAdmin)
