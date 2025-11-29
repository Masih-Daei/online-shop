"""
URL configuration for Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from Shop import settings
from .views import home , header ,footer,login_page,register_page,log_out
from products.views import ProductsList, products_categories_partial
from contact.views import contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('header',header,name='header'),
    path('footer',footer,name='footer'),
    path('login',login_page,name='login'),
    path('register',register_page,name='register'),
    path('logout',log_out,name='logout'),
    path('',include('products.urls',namespace='products')),
    path('',include('order.urls',namespace='order')),
    path('',include('Profile.urls',namespace='Profile')),
    path('products_categories_partial',products_categories_partial,name='products_categories_partial'),
    path('contact',contact_page,name='contact')
   
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)