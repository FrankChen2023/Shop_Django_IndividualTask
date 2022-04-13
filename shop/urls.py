from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'shop'

urlpatterns = [
        path('', views.general.index, name='index'),
        path('log_in/', views.general.log_in, name='log_in'),
        path('signup/', views.general.sign_up, name='sign_up'),
        path('product_search/', views.products.product_search, name='product_search'),
        path('product_add/', views.products.product_add, name='product_add'),
        path('product_list/', views.products.product_list, name='product_list'),
]