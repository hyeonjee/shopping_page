from django.urls import path
from .views import *


app_name="products"
urlpatterns=[
    path('', home, name="home"),
    path('main', main, name="main"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('show/<int:id>/', show, name="show"),
    path('edit/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('create_review/<int:product_id>/', create_review, name="create_review"),
    path('delete_review/<int:review_id>/', delete_review, name="delete_review"),
    path('edit_review/<int:review_id>/', update_review, name="update_review"),
]

