from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)
    paginator = Paginator(product, 12)
    page = request.GET.get('page') 
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)
        paginator = Paginator(product, 12)
        page = request.GET.get('page') 
        try:  
          products = paginator.page(page)  
        except PageNotAnInteger:  
            # Если страница не является целым числом, поставим первую страницу  
          products = paginator.page(1)  
        except EmptyPage:  
            # Если страница больше максимальной, доставить последнюю страницу результатов  
          products = paginator.page(paginator.num_pages)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'page': page,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def product_main(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True).order_by('-created')
    paginator = Paginator(product, 4)
    page = request.GET.get('page') 
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/main.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_new(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True).order_by('-created')
    paginator = Paginator(product, 10)
    page = request.GET.get('page') 
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/new.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_brends(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)
    paginator = Paginator(product, 15)
    page = request.GET.get('page') 
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/brends.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_sweets(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)
    paginator = Paginator(product, 15)
    page = request.GET.get('page') 
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/history_sweets.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)
    paginator = Paginator(product, 15)
    page = request.GET.get('page') 
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/shop_ios.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})