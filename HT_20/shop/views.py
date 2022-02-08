from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from cart.forms import CartAddProductForm
from .models import Category, Product
from .forms import ProductEditForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})


def product_edit(request, id, slug):
    if request.user.is_superuser:
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        if request.method == 'POST':
            product_edit_form = ProductEditForm(request.POST)
            if product_edit_form.is_valid():
                cd = product_edit_form.cleaned_data
                product.__dict__.update(cd)
                product.save(update_fields=cd.keys())
                messages.success(request, 'Інформацію про продукт змінено.')
                return redirect('shop:product_detail', id, slug)
            else:
                messages.error(request, 'Помилка. Спробуйте ще раз або пізніше.')
        else:
            product_edit_form = ProductEditForm(instance=product)
        context = {'form': product_edit_form}
        return render(request, 'shop/product/edit.html', context=context)
    else:
        messages.warning(request, 'У вас немає відповідних прав.')
        return redirect('shop:product_list')


def product_remove(request, id, slug):
    if request.user.is_superuser:
        product = get_object_or_404(Product, id=id, slug=slug)
        product.delete()
        messages.success(request, 'Продукт видалено')
    else:
        messages.warning(request, 'У вас немає відповідних прав.')
    return redirect('shop:product_list')
