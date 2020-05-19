from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Sum
from .models import Pizza,Topping,Subs,Pasta,Salad,Dinnerplatter,Cart,Orderhistory,Topping
from django.views.generic.list import ListView
from django.contrib.auth.mixins import (PermissionRequiredMixin )
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    
    total_order=Cart.objects.values_list('item_price', flat=True).filter(user=request.user,status='initiated')
    total = sum(total_order)
    tops=Topping.objects.all()
    context = {
        "user": request.user,
        'pizza':Pizza.objects.all(),
        #'topping':Topping.objects.all(),
        'subs':Subs.objects.all(),
        'pasta':Pasta.objects.all(),
        'salad':Salad.objects.all(),
        'dinnerplatter':Dinnerplatter.objects.all(),
        'cart':Cart.objects.all(),
        'total':total,
        'tops':tops
    }
    return render(request, "orders/home.html",context)



def additem(request):
    name=request.POST['name']
    price=float(request.POST['price'])
    try:
        pastatopping1=request.POST['pepperoni']
    except:
        pastatopping1=''
    try:
        pastatopping2=request.POST['olives']
    except:
        pastatopping2=''
        
    try:
        size=request.POST['size']
    except:
        size=''
        
    try:
        extra=request.POST['ppp']
    except:
        extra=''
    
    #condition for special pizza
    if name == 'Special Pizza':
        extra='Pepperoni, Fajita, Olives'
        
    #condition for Pasta checkboxes
    if name == 'Baked Ziti w/Chicken':
        if pastatopping1:
            extra=pastatopping1
            price=price+.5
        if pastatopping2:
            extra=extra+' & '+pastatopping2
            price=price+.5
   
    cart=Cart(
        user=request.user,
        cart_item=name,
        item_price=price,
        size=size,
        extras=extra
    )
    cart.save()
    return HttpResponseRedirect(reverse('index'))



def cart(request):
    total_order=Cart.objects.values_list('item_price', flat=True).filter(user=request.user,status='initiated')
    total = sum(total_order)
    total_stripe=total*100
    
    
    
    
    tops=Topping.objects.all()
    context = {
        'cart':Cart.objects.filter(user=request.user,status='initiated'),
         'total':total,
         'tops':tops,
         'total_stripe':total_stripe,
         
    }
    return render(request, "orders/cart.html",context)
      
      
      
def place_order(request):
    orderr=Cart.objects.filter(user=request.user,status='initiated').update(status='completed')
    #send_mail('Pizzashop', 'Hye you received a new order', 'umerjaved178@gmail.com', ['umerjaved178@yahoo.com'], fail_silently=False)
    #orderhist=Orderhistory.objects.get(user=request.user)
    #orderhist.save()
    return HttpResponseRedirect(reverse('index'))

    
        
def deletecartitem(request,id):
    dell=get_object_or_404(Cart,pk=id).delete()
    return HttpResponseRedirect(reverse('cart'))
    

@permission_required('orders.special_status')
def orders_page(request):
    cart=Cart.objects.filter(status='completed')
    context={
        'cart':cart
    }
    return render(request,"orders/orders_admin_page.html",context)


def userhistory(request):
    cart=Cart.objects.filter(user=request.user,status='completed')
    context={
        'cart':cart
    }
    return render(request,'orders/userhistory.html',context)


def changestatus(request,id):
    cart=Cart.objects.filter(user=request.user,id=id).update(delivery='delivered')
    return HttpResponseRedirect(reverse('orders_page'))
        









def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form=UserCreationForm()

    context={"form":form}
    return render(request,"orders/register.html",context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

