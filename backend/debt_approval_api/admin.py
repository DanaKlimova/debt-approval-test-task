from django.contrib import admin

from .models import Contract, DebtRequest, Item, Manufacturer

admin.site.register(Contract)
admin.site.register(DebtRequest)
admin.site.register(Item)
admin.site.register(Manufacturer)
