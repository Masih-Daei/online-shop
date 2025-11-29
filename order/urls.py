from django.urls import path
from . import views
app_name = 'order'
urlpatterns = [
    path('add_new_order',views.add_new_order,),
    path('cart',views.cart,name='cart'),
    path('remove_cart/<detail_id>',views.remove_cart,name='remove_cart')
]
