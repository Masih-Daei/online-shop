import os
import random
from django.db import models
def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image(instance, filename):
    rand_name = random.randint(1, 99999999999999)
    name, ext = get_file_extension(filename)
    final_name = f"{rand_name}{ext}"
    return f"settings/{final_name}"

# Create your models here.
class Settings(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    fax = models.CharField(max_length=130)
    address = models.TextField()
    copy_right = models.CharField(max_length=100)
    about = models.TextField()
    instagram = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=upload_image,null=True,blank=True)