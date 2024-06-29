from itertools import product

from django.contrib import admin
from .models import *
# Register your models here.



class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }

admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(Product, ProductModelAdmin)

