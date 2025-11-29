
from django.urls import include, path
from .views import ProductsList ,SearchProducts,ProductsListByCategory
from . import views

app_name = 'products'

urlpatterns = [
    path('products',ProductsList.as_view(),name='products_list'),
    path('products/<product_id>/<title>',views.product_detail,name='product_detail'),
    path('products/search', SearchProducts.as_view()),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    
   
]