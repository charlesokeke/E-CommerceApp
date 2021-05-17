from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def store(request, has_category_name=None):
    print(has_category_name)
    if has_category_name:
        category_id = get_object_or_404(Category, slug=has_category_name)
        products = Product.objects.all().filter(category=category_id, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    context = {
        'products':products,
        'total': len(products),
    }
    return render(request, 'store/store.html', context)


def product_detail(request, has_category_name, product_slug):

    try:
        single_product_detail = Product.objects.get(category__slug=has_category_name, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product_detail': single_product_detail,
    }
    return render(request, 'store/product_detail.html', context)
