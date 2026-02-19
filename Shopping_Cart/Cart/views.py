from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart, CartItem
from .forms import CartItemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')  # redirect after login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


def get_user_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

@login_required
def product_list(request):
    products = Product.objects.all()
    form = CartItemForm()
    return render(request,'product_list.html', {
        'products': products,
        'form': form
    })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_user_cart(request.user)

    form = CartItemForm(request.POST)
    if form.is_valid():
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )
        if not created:
            cart_item.quantity += form.cleaned_data['quantity']
        else:
            cart_item.quantity = form.cleaned_data['quantity']
        cart_item.save()
        messages.success(request, "Product added to cart")

    return redirect('view_cart')


@login_required
def view_cart(request):
    cart = get_user_cart(request.user)
    return render(request, 'cart.html', {
        'cart': cart,
        'items': cart.items.all(),
        'total': cart.total_price()
    })


@login_required
def update_cart(request, item_id):
    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    form = CartItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, "Cart updated")

    return redirect('view_cart')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )
    item.delete()
    messages.info(request, "Item removed")
    return redirect('view_cart')


