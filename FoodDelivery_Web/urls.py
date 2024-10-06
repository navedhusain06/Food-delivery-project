"""
URL configuration for FoodDelivery_Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from FoodDelivery_App.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeFun, name='hnm'),
    path('login/', loginFun, name='lnm'),
    path('register/', registerFun, name='rnm'),
    path('logout/', logoutFun, name='onm'),
    path('add-cart/<pizza_uid>/', add_cart, name='add_cart'),
    path('cart/', cart, name='cart'),
    path('remove_cart_items/<cart_item_uid>', remove_cart_items, name='remove_cart_items'),
    path('orders/', orders, name='orders'),
    path('app/', include('FoodDelivery_App.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

