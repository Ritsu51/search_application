from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Favorite


from .models import Product
# Register your models here

admin.site.register(Product)
admin.site.register(Favorite)
admin.site.unregister(Group)