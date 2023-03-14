from django.contrib import admin
from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'email', 'phone_number')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class ServiceOrderInline(admin.TabularInline):
    model = models.ServiceOrder
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'customer', 'status', 'total_order_price')
    list_filter = ('status', 'date')
    list_editable = ('status', )
    inlines = (ServiceOrderInline, )

class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('service', 'quantity', 'total_price')
    list_display_links = ('service', )

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.ServiceOrder, ServiceOrderAdmin)
