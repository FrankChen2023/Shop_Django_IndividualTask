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
        path('product_add/', views.products.product_add, name='product_add'),
        path('product_list/', views.products.product_list, name='product_list'),
        path('product_search/', views.products.product_search, name='product_search'),
        path('balance/', views.customer.customer_balance, name='balance'),
        path('basket_add/', views.basket.basket_add, name='basket_add'),
        path('basket_detail/<str:basketname>/', views.basket.basket_detail, name='basket_detail'),
        path('basket_edit/<int:id>/', views.basket.basket_edit, name='basket_edit'),
        path('basket_delete/<int:id>/', views.basket.basket_delete, name='basket_delete'),
        path('basket_delete_success/', views.basket.basket_delete_success, name='basket_delete_success'),
        path('basket_payment/<int:id>/', views.basket.basket_payment, name='basket_payment'),
        path('/<str:basketname>/', views.item.item_add, name='item_add'),
        path('item_list/', views.item.item_list, name='item_list'),
        path('item_edit/<int:id>', views.item.item_edit, name='item_edit'),
        path('item_delete/<int:id>', views.item.item_delete, name='item_delete'),
        path('/<str:basketname>/<int:id>/', views.item.item_detail, name='item_detail'),
]