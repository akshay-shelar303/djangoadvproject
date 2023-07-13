from django.contrib import admin

from .models import ElectronicItems


class ElectronicModel(admin.ModelAdmin):
    list_display = ["id", "name", "description", "image", "price"]


admin.site.register(ElectronicItems, ElectronicModel)
