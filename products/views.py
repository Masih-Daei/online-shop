
from django.http import Http404
from django.shortcuts import render

from category.models import ProductCategory
from .models import Products
from django.views.generic.list import ListView
from .models import Products, ProductGallery
from order.forms import UserNewOrderForm
# Create your views here.


class ProductsList(ListView):
    template_name = 'products_list.html'
    paginate_by = 1

    def get_queryset(self):
        return Products.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products_list.html'
    paginate_by = 4

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        categories = ProductCategory.objects.filter(name__iexact=category_name)
        if categories is None:
            raise Http404('page not found ):')
        return Products.objects.get_product_by_category(category_name)


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category.html', context)


def product_detail(request, *args, **kwargs):
    product_id = kwargs['product_id']
    title = kwargs['title']
    new_user_form = UserNewOrderForm(request.POST or None,initial=({'product_id':product_id}))

    product = Products.objects.get_product_by_id(product_id)
    if product is None:
        raise Http404('محصول مورد نظر یافت نشد')
    
    product.visits =+ 1
    product.save()

    gallery = ProductGallery.objects.filter(product_id=product_id)

    related_product= Products.objects.filter(categories__in=product.categories.all()).exclude(id=product.id)

    context = {
        'product': product,
        'gallery': gallery,
        'related_product':related_product ,
        'new_user_form':new_user_form
    }
    return render(request, 'product_detail.html', context)


class SearchProducts(ListView):
    template_name = 'products_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        if query is not None:
            return Products.objects.search_products(query)

        return Products.objects.get_active_products()
