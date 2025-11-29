from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.title