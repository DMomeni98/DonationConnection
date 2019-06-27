from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.


# def products(request):
#     return render(request, "addproduct.html", {})
# ---------------------------------------------------Temp-------------------------------------------------

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form
    }

    return render(request, 'addproduct.html', context)


# def product_list(request):
    # # category = None
    # # categories = Category.objects.all()
    # products = Product.objects.filter(available=True)
    # return render(request, 'addproduct.html   ',
    #               {'products': products})


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/details.html',
#                   {'product': product, 'cart_product_form': cart_product_form})