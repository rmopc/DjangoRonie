# Jos rekisteröi tällä tavalla adminille oman appin
# modelit, voi myös admin sivuilta muokata näitä tietoja.

from django.contrib import admin
from app.models import Supplier, Product, Distributor, Location

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass    