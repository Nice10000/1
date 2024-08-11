from django.contrib import admin # type: ignore
from .models import Category, unit, Item, Supplier, order

# Register your models here.
admin.site.register(Category)
admin.site.register(unit)
admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(order)



