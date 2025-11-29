from django.shortcuts import render, redirect

from order.models import Order_Detail , Order
from sliders.models import Slider
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login ,get_user_model,logout
from settings.models import Settings
from products.models import Products
def home(request):
    featured = Products.objects.filter(featured = True)
    slider = Slider.objects.all()
    most_visit_product = Products.objects.order_by('-visits').all()
    latest_products = Products.objects.order_by('-id').all()
    context = {
        'slider':slider,
        'featured':featured,
        'most_visit_product':most_visit_product,
        'latest_products':latest_products
    }
    return render(request, 'home.html', context)


def header(request):
    settings = Settings.objects.first()
    
    open_order = None
    order_items = []
    total_price = 0
    
    if request.user.is_authenticated:
        open_order = Order.objects.filter(user_id=request.user.id, paid=False).first()
        if open_order:
            order_items = open_order.order_detail_set.all()  
            total_price = open_order.total_price() if hasattr(open_order, 'total_price') else 0
    
    context = {
        'settings': settings,
        'order': order_items,  
        'total_price': total_price
    }
    
    return render(request, 'base/header.html', context)

def footer(request):
    settings = Settings.objects.first()
    context = {
        'settings':settings
    }
    return render(request, 'base/footer.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        userName = login_form.cleaned_data.get('userName')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')

    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        userName = register_form.cleaned_data.get('userName')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        new_user = User.objects.create_user(
            username=userName, email=email, password=password)
        print(new_user)

    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)

def log_out(request):
    logout(request)
    return redirect('login')