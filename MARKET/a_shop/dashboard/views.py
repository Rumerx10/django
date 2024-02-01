from django.shortcuts import render,get_object_or_404, redirect
from item.views import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

@login_required
def index(request):
    items = Item.objects.filter(created_by = request.user)
    
    return render(request, 'dashboard.html', {'items':items})

@login_required
def logout_site(request):
    logout(request)
    return redirect('/')