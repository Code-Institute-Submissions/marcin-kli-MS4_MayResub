from django.contrib import admin
from .models import Packages, Category


class PackagesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
    )

    ordering = ('name',)


admin.site.register(Packages, PackagesAdmin)
admin.site.register(Category)
