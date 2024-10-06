from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', homeFun, name='hnm'),
    path('login/', loginFun, name='lnm'),
    path('register/', registerFun, name='rnm'),
    path('add-cart/<pizza_uid>/', add_cart, name='add_cart'),
    path('cart/', cart, name='cart'),
    path('orders/', orders, name='orders'),
    
    
] 