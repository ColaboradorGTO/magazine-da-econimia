from django.contrib import admin

# Product model 
from . models import *

# Register your models here.

admin.site.register(Offer)
admin.site.register(Category)
admin.site.register(Product)






