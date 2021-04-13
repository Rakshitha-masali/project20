from django.urls import path
from app1 import views
app_name="app1"

urlpatterns=[
    path('',views.index,name="index"),
    path('sample/',views.sample,name="sample"),
    path("<data>/",views.carry_data,name="carry_data"),
    

]
