from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=500,unique=True)
    slug=models.SlugField(max_length=500,unique=True)
    description=models.TextField(max_length=1000,blank=True)
    cat_image=models.ImageField(upload_to='images/categories',blank=True)

    class Meta:
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    subcat_image = models.ImageField(upload_to='images/subcategories', blank=True)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def get_url(self):
        return reverse('products_by_subcategory', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.subcategory_name

