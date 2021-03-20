from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'street_address1', 'street_address2', 'town', 'country',
              'postcode', 'email', 'phone_number', 'total',)

    list_display = ('order_number', 'full_name', 'date', 'total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
