from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20,blank=True,unique=True)
    image = models.ImageField(upload_to='media/')
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        super(Category,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
    
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    image = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True,blank=True)
    price = models.CharField(max_length=10)
    oldPrice = models.CharField(max_length=10)
    info = models.TextField(max_length=1000)
    rating = models.CharField(max_length=4)
    image = models.ImageField(upload_to='media/')
    created_date = models.DateTimeField(auto_now=True)
    images = models.ManyToManyField(Image,related_name='product_images')
    category = models.ForeignKey(Category,related_name='categroy',on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        super(Product,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.CharField(unique=True,max_length=50)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    orderno = models.CharField(max_length=15)
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    products = models.JSONField()
    address = models.JSONField()
    orderdate = models.DateTimeField(auto_now=True)
    deliverydate = models.CharField(max_length=20)
    
