from django.shortcuts import render, redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def home(request):
 return render(request, 'app/home.html')


class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request, 'app/home.html',{
            'topwears':topwears,
            'bottomwears':bottomwears,
            'mobiles':mobiles
        })


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product':product,'item_already_in_cart':item_already_in_cart})



@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    cart = Cart(user=user, product=product).save()
    return redirect('home')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)  
        shipping_charge = 70.0
        total_amount = 0.0
        temp_amount = 0
        
        # cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart:            
            for p in cart:
                temp_amount = temp_amount +  (p.quantity*p.product.discounted_price)
            total_amount = temp_amount+shipping_charge        
        else:
            return render(request, 'app/empty.html')      
        return render(request, 'app/addtocart.html', {'carts':cart, 'temp_amount':temp_amount,'total_amount':total_amount})
    


def plus_cart(request):
    if request.method=='GET':
        product_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        
        cart = Cart.objects.filter(user=request.user)  
        shipping_charge = 70.0
        total_amount = 0.0
        temp_amount = 0
        for p in cart:
            temp_amount = temp_amount +  (p.quantity*p.product.discounted_price)
        total_amount = temp_amount+shipping_charge
        
        data = {
            'quantity':c.quantity,
            'temp_amount':temp_amount,
            'total_amount':total_amount
        }        
    return JsonResponse(data)


def minus_cart(request):
    if request.method=='GET':
        product_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        if c.quantity>1:
            c.quantity -= 1
        c.save()
        
        cart = Cart.objects.filter(user=request.user)  
        shipping_charge = 70.0
        total_amount = 0.0
        temp_amount = 0
        for p in cart:
            temp_amount = temp_amount +  (p.quantity*p.product.discounted_price)
        total_amount = temp_amount+shipping_charge
        
        data = {
            'quantity':c.quantity,
            'temp_amount':temp_amount,
            'total_amount':total_amount
        }        
    return JsonResponse(data)


def remove_cart(request):
    if request.method=='GET':
        product_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.delete()
        
        cart = Cart.objects.filter(user=request.user)
        shipping_charge = 70.0
        total_amount = 0.0
        temp_amount = 0
        for p in cart:
            temp_amount = temp_amount +  (p.quantity*p.product.discounted_price)
        total_amount = temp_amount+shipping_charge
        
        data = {
            'temp_amount':temp_amount,
            'total_amount':total_amount
        }        
    return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
    address = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'address':address,'active':'btn-primary'})


@login_required
def orders(request):
    orders = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'orders':orders})


def mobile(request, data=None):    
    brands = ['Samsung','Vivo','Nubia','IQoo','Apple','Xiaomi','Redmi','Oppo','Realme','Honor'] 
    if data == None:
        mobiles = Product.objects.filter(category="M")
    elif data in brands:
        mobiles = Product.objects.filter(category="M").filter(brand=data) 
    elif data == 'below':
        mobiles = Product.objects.filter(category="M").filter(discounted_price__lt=10000) 
    elif data == 'above':
        mobiles = Product.objects.filter(category="M").filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html',{"mobiles":mobiles})

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation ! Registration Successfull')
            form.save()
            # return redirect('login')
        return render(request, 'app/customerregistration.html', {'form':form})
              
@login_required
def checkout(request):
    user = request.user
    address = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    shipping_charge = 70.0
    total_amount = 0.0
    temp_amount = 0
    if cart_items:
        for p in cart_items:
            temp_amount = temp_amount +  (p.quantity*p.product.discounted_price)
        total_amount = temp_amount+shipping_charge
    return render(request, 'app/checkout.html',{'address':address,'cart_items':cart_items,'total_amount':total_amount})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity = c.quantity).save()
        c.delete()
    return redirect('orders')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,'Profile updated successfully!')
            
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})