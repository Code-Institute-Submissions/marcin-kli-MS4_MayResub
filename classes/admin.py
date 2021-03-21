from django.contrib import admin
from .models import Classes

# Register your models here.


class ClassesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image_url',
        'image',
    )

    ordering = ('name',)


admin.site.register(Classes, ClassesAdmin)
