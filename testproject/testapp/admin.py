from django.contrib import admin
from .models import Product, Lesson, ProductAccess

admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(ProductAccess)
