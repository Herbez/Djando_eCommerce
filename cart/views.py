from django.shortcuts import render, get_object_or_404
from .cart import Cart
from e_shop.models import Product
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    username = None 	
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'cart_page.html',
        {'username': username, "cart_products":cart_products})
    else:
        return render(request, 'cart_page.html')
    
def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		response = JsonResponse({'Product Name: ': product.name})

		
		return response
      
def cart_delete(request):
    pass
def cart_update(request):
    pass
