from django.contrib import admin
from users.models import *
# Register your models here.

admin.site.register(Profile)



class CustCartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'prod_code', 'quantity', 'username')

admin.site.register(CustCart, CustCartAdmin)