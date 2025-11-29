from django.db import models
from django.contrib.auth.models import User

from products.models import Products
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    pay_date = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return self.user.get_full_name()
    
    def total_price(self):
        amount = 0
        for detail in self.order_detail_set.all():
            amount += detail.price * detail.count
        return amount

    
class Order_Detail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return self.product.title
    
    def product_sum_in_cart(self):
        return self.price * self.count