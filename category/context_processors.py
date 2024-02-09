from .models import Category,Subcategory


def menu_links(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return {'categories': categories, 'subcategories': subcategories}
