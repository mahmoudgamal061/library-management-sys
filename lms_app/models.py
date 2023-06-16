from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    status_book=[
        ('available','available'),
        ('sold','sold'),
        ('rental','rental'),
    ]
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50,blank=True, null=True)
    price=models.DecimalField(max_digits=6,decimal_places=2,blank=True, null=True)
    retal_price_day=models.DecimalField(max_digits=6,decimal_places=2,blank=True, null=True)
    retal_period=models.IntegerField(blank=True, null=True)
    total_rental=models.DecimalField(max_digits=6,decimal_places=2,blank=True, null=True)
    active=models.BooleanField(default=True)
    photo_book=models.ImageField(upload_to='photos/%y/%m/%d', null=True,blank=True)
    photo_author=models.ImageField(upload_to='photos/%y/%m/%d', null=True,blank=True)
    pages=models.IntegerField(blank=True, null=True)
    status=models.CharField(max_length=50,choices=status_book,blank=True, null=True)
    category=models.ForeignKey(Category , on_delete=models.PROTECT,blank=True, null=True )
    slug=models.SlugField(unique=True,blank=True, null=True)
    
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Book,self).save(*args,**kwargs)
        
    