from django.contrib import admin
from users.models import *
# Register your models here.

admin.site.register(Profile)



class CustCartAdmin(admin.ModelAdmin):
    list_display = ('username','prod_code', 'cart_id', 'quantity', )

admin.site.register(CustCart, CustCartAdmin)




class CustRatingFeedbackAdmin(admin.ModelAdmin):
    list_display = ('username','prod_code', 'ratings' )

admin.site.register(CustRatingFeedback, CustRatingFeedbackAdmin)


class PlacedOrdersAdmin(admin.ModelAdmin):
    list_display = ('user','order_id','prod_code', 'quantity' )

admin.site.register(PlacedOrders, PlacedOrdersAdmin)