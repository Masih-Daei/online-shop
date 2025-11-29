from django.urls import path
from . import views
app_name = 'Profile'
urlpatterns = [
    path('profile',views.profile_main_page,name='profile'),
    path('profile/orders', views.profile_user_order, name="orders"),
    path('profile/setting', views.profile_setting, name="setting"),

]
