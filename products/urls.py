from django.urls import path
from .views import *


app_name="products"
urlpatterns=[
    path('', main, name="main"),
    path('item_category/', item_category, name="item_category"),
    path('new/', new, name="new"),
    path('show/', show, name="show"),
    
  
]

