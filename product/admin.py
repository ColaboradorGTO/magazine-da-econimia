from django.contrib import admin

# Product model 
from . models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)






