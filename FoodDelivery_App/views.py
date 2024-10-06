from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages

# from instamojo_wrapper import Instamojo



# Create your views here.

def homeFun(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas':pizzas
    }
    return render(request, 'home.html', context)

def loginFun(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        
        if not user_obj.exists():
            messages.warning(request, 'User Does not Exists')
            return redirect('lnm')
        
        user_obj = authenticate(username = email, password = password)
        if user_obj:
            login(request, user_obj)
            return redirect('hnm')
        messages.error(request, 'Incorrect password')
        return redirect('lnm')
    return render(request, 'login.html')



def registerFun(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        
        if user_obj.exists():
            messages.warning(request, 'Email already exists')
            return redirect('rnm')
        
        user_obj = User.objects.create(first_name=firstname, last_name=lastname, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'Your account Successfully are created')
        return redirect('lnm')

    
    return render(request, 'register.html')

def logoutFun(request):
    logout(request)
    return redirect('hnm')

def add_cart(request, pizza_uid):
    user = request.user
    pizza_obj = Pizza.objects.get(uid = pizza_uid)
    cart, _ = Cart.objects.get_or_create(user = user, is_paid = False)
    cart_items = CartItems.objects.create(
        cart=cart,
        pizza = pizza_obj
    )
    return redirect('/')

def cart(request):
    cart = Cart.objects.get(is_paid = False, user = request.user)
    context = {'cart':cart}
    
    return render(request, 'cart.html',context )


def remove_cart_items(request, cart_item_uid):
    try:
        CartItems.objects.get(uid = cart_item_uid).delete()
        return redirect('cart')
    
    except Exception as e:
        print(e)
    
    
def orders(request):
    orders = Cart.objects.filter(is_paid=True, user = request.user)
    context = {'orders':orders}
    return render(request, 'order.html', context)

# def process_payment(request):
