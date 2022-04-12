from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'shop'

urlpatterns = [
        path('product_add/', views.products.product_add, name='product_add'),
        path('', views.products.product_list, name='product_list'),

]