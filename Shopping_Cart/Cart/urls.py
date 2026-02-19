"""
URL configuration for Shopping_Cart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('products/', views.product_list, name='product_list'), 
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
   # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('cart/', views.view_cart, name='view_cart'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
#     path('remove-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]
