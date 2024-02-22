from django.urls import path, include
from users import views as userviews

app_name = 'users'


urlpatterns = [
    #profile form editing
    path('profformedit/<int:userid>/', userviews.ProfileFormEdit, name='profformedit'),
    
    #profile form creating
    path('profformcreate/<int:userid>/', userviews.ProfFormCreate, name='profformcreate'),
    
    #cart item create
    path('cart/<int:itemid>/<int:pdcd>/<str:user>/', userviews.CustCartView, name='cart'),

]