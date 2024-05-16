from django.contrib import admin

from .models import MasterChef, ProductType, FoodMenu, TableOnline, Costumer, Testimonial
admin.site.register(MasterChef)
admin.site.register(ProductType)
admin.site.register(FoodMenu)
admin.site.register(TableOnline)
admin.site.register(Costumer)
admin.site.register(Testimonial)
