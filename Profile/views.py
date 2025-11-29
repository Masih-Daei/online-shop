from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from order.models import Order
from .forms import UserEditProfileForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login')
def profile_main_page(request):
    context ={}
    return render(request,'profile.html',context)

@login_required(login_url='/login')
def profile_user_order(request):
    open_order = None
    order_items = []
    total_price = 0
    
    if request.user.is_authenticated:
        open_order = Order.objects.filter(user_id=request.user.id, paid=False).first()
        if open_order:
            order_items = open_order.order_detail_set.all()  
            total_price = open_order.total_price() if hasattr(open_order, 'total_price') else 0
    
    context = {
        'order': order_items,  
        'total_price': total_price
    }
    return render(request,'profile_order.html',context)

@login_required(login_url='/login')
def profile_sidebar(request):
    context ={}
    return render(request,'profile_sidebar.html',context)

@login_required(login_url='/login')
def profile_setting(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()

    edit_form = UserEditProfileForm(request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
    if edit_form.is_valid():
        first_name = edit_form.cleaned_data.get('first_name')
        last_name = edit_form.cleaned_data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {
        'edit_form': edit_form
    }
    return render(request, 'profile_setting.html', context)