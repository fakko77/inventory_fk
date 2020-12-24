from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Brand


def index(request):
    """view return home page"""
    if request.user.is_authenticated:
        return render(request, 'app_inventory_fk/index.html')
    else:
        return render(request, 'app_inventory_fk/login.html')


def login(request):
    """view for login"""
    return render(request, 'app_inventory_fk/login.html')


def check(request):
    """form post login and check user"""
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(
        username=username, password=password)
    if user is not None and user.is_active:
        auth_login(request, user)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'app_inventory_fk/login.html')


def setting(request):
    """add new items, department, brand, type , modelItem  """
    brand = Brand.objects.all()

    context = {
        'brand': brand
    }
    return render(request, 'app_inventory_fk/setting.html', context)
