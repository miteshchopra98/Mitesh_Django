from django.urls import path
from food import views
app_name = 'food'

urlpatterns = [
    path('home/', views.Index, name ='Index'),
    path('detail/<int:itemid>/', views.Detail, name ='detail'),
    path("add/", views.CreateItem, name="createitem"),
    path('update/<int:itemid>', views.UpdateItem, name='updateitem'),
    path('delete/<int:itemid>', views.DeleteItem, name='deleteitem'),
]
