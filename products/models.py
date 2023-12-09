from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Choises(models.Model):
    options = models.CharField(max_length=50, null=False, blank=False)
    
class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            if not Category.objects.filter(slug=slugify(self.title)).exists():
                self.slug = slugify(self.title)
                super().save(*args, **kwargs)
            else:
                raise ValueError('Ya existe una categoria con ese nombre')

class Products(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    price = models.DecimalField(blank=False, null=False, max_digits=6, decimal_places=2)
    discount = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=False)
    choises = models.ManyToManyField(Choises)
    slug = models.SlugField(blank=True, null=False)
    port_img = models.ImageField(upload_to='products/files/port')
    firts_img = models.ImageField(upload_to='products/files/baner')
    second_img = models.ImageField(upload_to='products/files/baner', blank=True, null=True)
    third_img = models.ImageField(upload_to='products/files/baner', blank=True, null=True)
    four_img = models.ImageField(upload_to='products/files/baner', blank=True, null=True)
    sold = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            if not Products.objects.filter(slug=slugify(self.title)).exists():
                self.slug = slugify(self.title)
                super().save(*args, **kwargs)
            else:
                raise ValueError('Ya existe un producto con ese nombre')