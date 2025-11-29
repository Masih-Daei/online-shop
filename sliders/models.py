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
    final_name = f"{instance.id}-{instance.title}-{rand_name}{ext}"
    return f"products/{final_name}"

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to=upload_image,null=True,blank=True)

    def __str__(self):
        return self.title