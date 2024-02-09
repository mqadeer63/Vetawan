from django.db import models
from django.urls import reverse
from category.models import Category,Subcategory

# Create your models here.
class Product(models.Model):
    product_name= models.CharField(max_length=450,unique=True)
    slug=models.SlugField(max_length=450,unique=True)
    short_description= models.TextField(max_length=800,unique=True)
    product_description= models.TextField(max_length=1500,blank=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/product')
    stock= models.IntegerField()
    is_available= models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                                    null=True, blank=True,)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def get_url(self):
        if self.subcategory:
            return reverse('product_detail', args=[self.category.slug, self.subcategory.slug, self.slug])
        else:
            return reverse('product_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice=(
    ('size','size'),
)

class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=variation_category_choice)
    variation_value=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)

    objects=VariationManager()

    def __str__(self):
        return self.variation_value
    