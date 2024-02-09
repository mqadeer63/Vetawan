from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from carts.models import Cart,CartItem
from carts.views import _cart_id
from .models import Product
from category.models import Category,Subcategory
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers  import ProductSerailizer,CategorySerailizer,SubcategorySerailizer
# Create your views here.


@api_view(['GET'])
def store(request,category_slug=None,subcategory_slug=None):
    categories=None
    subcategory = None
    subcategories = None
    products=None
    if category_slug != None:
        categories=get_object_or_404(Category,slug=category_slug)
        subcategories = Subcategory.objects.filter(category=categories)
        subcategory = None 
        if subcategory_slug:
            subcategory = get_object_or_404(Subcategory, slug=subcategory_slug, category=categories)
            products = Product.objects.filter(category=categories, subcategory=subcategory, is_available=True)
        else:  
            products=Product.objects.filter(category=categories,is_available=True)
            paginator=Paginator(products,1)
            page=request.GET.get('page')
            paged_products=paginator.get_page(page)
            product_count = products.count()
    else:
       
        products= Product.objects.all().filter(is_available=True).order_by('id')
        serializer=ProductSerailizer(products,many=True)
        paginator=Paginator(products,1)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)

        product_count= products.count()
    
    context = {
        'categories': categories,
        'subcategories': subcategories,
        'subcategory': subcategory,
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request,'store.html',context)
    
# def store_api(request, category_slug=None, subcategory_slug=None):
#     categories = None
#     subcategories = None
#     subcategory = None
#     products = None

#     if category_slug:
#         categories = get_object_or_404(Category, slug=category_slug)
#         subcategories = Subcategory.objects.filter(category=categories)
#         subcategory = None

#         if subcategory_slug:
#             subcategory = get_object_or_404(Subcategory, slug=subcategory_slug, category=categories)
#             products = Product.objects.filter(category=categories, subcategory=subcategory, is_available=True)
#         else:
#             products = Product.objects.filter(category=categories, is_available=True)

#     else:
#         products = Product.objects.all().filter(is_available=True).order_by('id')

#     paginator = Paginator(products, 1)
#     page = request.GET.get('page')
#     paged_products = paginator.get_page(page)
#     product_count = products.count()

#     # Serialize data
#     categories_data = None
#     subcategories_data = None
#     subcategory_data = None
#     products_data = None

#     if categories:
#         categories_data = {
           
#             'name': categories.category_name,
#             'slug': categories.slug,
#             # Add other fields as needed
#         }

#     if subcategories:
#         subcategories_data = [{'name': sub.subcategory_name, 'slug': sub.slug} for sub in subcategories]

#     if subcategory:
#         subcategory_data = {
#             # 'id': subcategory.id,
#             'name': subcategory.subcategory_name,
#             'slug': subcategory.slug,
#             # Add other fields as needed
#         }

#     if paged_products:
#         products_data = [{'name': prod.product_name, 'price': prod.price} for prod in paged_products.object_list]

#     context = {
#         'categories': categories_data,
#         'subcategories': subcategories_data,
#         'subcategory': subcategory_data,
#         'products': products_data,
#         'product_count': product_count,
#     }


#     return JsonResponse(context)

#     # return render(request, 'store.html', context)

def store_api(request, category_slug=None, subcategory_slug=None):
    categories = None
    subcategories = None
    subcategory = None
    products = None

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        categories_serializer = CategorySerailizer(categories)
        subcategories = Subcategory.objects.filter(category=categories)
        subcategory = None

        if subcategory_slug:
            subcategory = get_object_or_404(Subcategory, slug=subcategory_slug, category=categories)
            subcategory_serializer = SubcategorySerailizer(subcategory)
            products = Product.objects.filter(category=categories, subcategory=subcategory, is_available=True)
        else:
            subcategories_serializer = SubcategorySerailizer(subcategories, many=True)
            products = Product.objects.filter(category=categories, is_available=True)

    else:
        categories = Category.objects.all()  # Fetch all categories
        categories_serializer = CategorySerailizer(categories, many=True)
        subcategories = Subcategory.objects.all()  # Fetch all subcategories
        subcategories_serializer = SubcategorySerailizer(subcategories, many=True)

        products = Product.objects.all().filter(is_available=True).order_by('id')

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    # Serialize data
    categories_data = None
    subcategories_data = None
    subcategory_data = None
    products_data = None

    if categories:
        categories_data = categories_serializer.data

    if subcategories:
        subcategories_data = subcategories_serializer.data

    if subcategory:
        subcategory_serializer = SubcategorySerailizer(subcategory)
        subcategory_data = subcategory_serializer.data

    if paged_products:
        products_serializer = ProductSerailizer(paged_products, many=True)
        products_data = products_serializer.data

    context = {
        'categories': categories_data,
        'subcategories': subcategories_data,
        'subcategory': subcategory_data,
        'products': products_data,
        'product_count': product_count,
    }

    return JsonResponse(context)

def product_detail(request,category_slug,product_slug,subcategory_slug=None):
    try:
        if subcategory_slug:
            single_product = Product.objects.get(category__slug=category_slug,
                                                 subcategory__slug=subcategory_slug, slug=product_slug)        
        else:
            single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
        
    except Exception as e:
        raise e
    context={
        'single_product':single_product,
        'in_cart':in_cart
    }
    return render(request,'store/product_detail.html',context)

def product_detail_api(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Product.DoesNotExist:
        # Handle the case when the product is not found
        return JsonResponse({'error': 'Product not found'}, status=404)
    except Exception as e:
        # Handle other exceptions
        return JsonResponse({'error': str(e)}, status=500)

    context = {
        'single_product': {
            'name': single_product.product_name,
            'description': single_product.product_description,
            # Add other fields as needed
        },
        'in_cart': in_cart
    }

    return JsonResponse(context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(product_name__icontains=keyword) | Q(product_description__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'keyword': keyword,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context=context)
