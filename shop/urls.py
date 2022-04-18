from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'shop'

urlpatterns = [
        path('', views.general.index, name='index'),
        path('log_in/', views.general.log_in, name='log_in'),
        path('log_out/', views.general.log_out, name='log_out'),
        path('sign_up/', views.general.sign_up, name='sign_up'),
        path('signup_success/', views.general.signup_success, name='signup_success'),
        path('login_success/', views.general.login_success, name='login_success'),
        path('/<str:basketname>/', views.item.item_add, name='item_add'),
        path('product_add/', views.products.product_add, name='product_add'),
        path('product_list/', views.products.product_list, name='product_list'),
        path('product_search/', views.products.product_search, name='product_search'),
        path('balance/', views.customer.customer_balance, name='balance'),
        path('basket_add/', views.basket.basket_add, name='basket_add'),
        path('basket_detail/<str:basketname>/', views.basket.basket_detail, name='basket_detail'),
        path('basket_edit/<str:basketname>/', views.basket.basket_edit, name='basket_edit'),
        path('item_list/', views.item.item_list, name='item_list'),
        path('/<str:basketname>/<int:id>/', views.item.item_detail, name='item_detail'),
]