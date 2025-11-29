from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from order.models import Order, Order_Detail
from products.models import Products
from .forms import UserNewOrderForm
# Create your views here.


@login_required(login_url='/login')
def add_new_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    
    if new_order_form.is_valid():
        order = Order.objects.filter(user_id=request.user.id, paid=False).first()
        if order is None:
            order = Order.order_detail_set.create(user_id=request.user.id, paid=False)

        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        

        product = Products.objects.get_product_by_id(product_id)
        if product is None:
            messages.error(request, "محصول مورد نظر یافت نشد!")
            return redirect('home')  

        if count < 0:
            count = 1


        existing_order_detail = Order_Detail.objects.filter(
            order=order,
            product_id=product.id
        ).first()

        if existing_order_detail:
            existing_order_detail.count += count
            existing_order_detail.save()
            messages.success(request, f"تعداد {product.title} به {existing_order_detail.count} افزایش یافت")
        else:
        
            order.order_detail_set.create( 
                product_id=product.id, 
                count=count, 
                price=product.price
            )
            messages.success(request, f"{product.title} به سبد خرید اضافه شد")

        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')
    
    else:

        messages.error(request, "خطا در افزودن به سبد خرید")
        return redirect('home')  
@login_required(login_url='/login')
def cart(request):
    context = {
        'order': None,
        'details': None,
        'total_price': 0 
    }
    open_order: Order = Order.objects.filter(user_id=request.user.id, paid=False).first()
    
    if open_order is not None:  
        context['order'] = open_order
        context['details'] = open_order.order_detail_set.all()
        context['total_price'] = open_order.total_price()

    return render(request, 'cart.html', context)


@login_required(login_url='/login')
def remove_cart(request, *args, **kwargs):
    detail_id = kwargs['detail_id']
    action = request.GET.get('action', 'remove_one')  
    
    try:
        order_detail = Order_Detail.objects.get(
            id=detail_id, 
            order__user_id=request.user.id,
            order__paid=False
        )
        
        if action == 'remove_one':
            if order_detail.count > 1:
                order_detail.count -= 1
                order_detail.save()
            else:
                order_detail.delete()
                
        elif action == 'remove_all':
            order_detail.delete()
            
        return redirect('/cart')
        
    except Order_Detail.DoesNotExist:
        raise Http404()
