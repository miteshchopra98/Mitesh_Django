from django.urls import path, include
from users import views as userviews

app_name = 'users'


urlpatterns = [
    path('profformedit/<int:userid>/', userviews.ProfileFormEdit, name='profformedit'),
    path('profformcreate/<int:userid>/', userviews.ProfFormCreate, name='profformcreate'),
    
]