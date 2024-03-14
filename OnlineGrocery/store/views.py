from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.cart import Cart
from django.contrib import messages
from django.views import View
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

def home(request):
    products = None
    total_item = 0
    if request.session.has_key('phone'):
        phone = request.session['phone']
        category = Category.get_all_categories()
        customer = Customer.objects.filter(phone=phone)
        total_item = len(Cart.objects.filter(phone=phone))
        for c in customer:
            name = c.name

            categoryID = request.GET.get('category')
            if categoryID:
                products = Product.get_all_product_by_category_id(categoryID)
            else:
                products = Product.get_all_products()

                data = {}
                data['name'] = name
                data['product'] = products
                data['category'] = category
                data['total_item'] = total_item
                return render(request, 'home.html', data)
    else:
        return redirect('login')




class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        phone = postData.get('phone')

        error_message = None
        value = {
            'name': name,
            'phone': phone
        }

        customer = Customer(name=name, phone=phone)

        if not name:
            error_message = 'Please enter a name'
        elif not phone:
            error_message = 'Please enter a contact number'
        elif len(phone) < 10:
            error_message = 'Please enter a valid contact number'
        elif customer.isExist():
            error_message = 'This contact number is already registered'

        if not error_message:
            messages.success(request, 'Registration successful !!!')
            customer.register()
            return redirect('signup')
        else:
            data = {
                'error': error_message,
                'value': value
            }
            return render(request, 'signup.html', data)

        
        



        

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        phone = request.POST.get('phone')
        error_message = None
        value = {
            'phone': phone
        }
        customer = Customer.objects.filter(phone=request.POST["phone"])
        if customer:
            request.session['phone'] = phone
            return redirect('homepage')
        else:
            error_message = 'Please enter a valid contact number'
            data = {
                'error': error_message,
                'value': value
            }

        return render(request, 'login.html', data)
    

def add_to_cart(request):
    phone = request.session['phone']
    product_id = request.GET.get('prod_id')
    product_name = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        image = p.image
        price = p.price
        Cart(phone=phone, product=product_name, image=image, price=price).save()
        return redirect(f"/product-details/{product_id}") 
    


def productdetails(request, pk):
         total_item = 0
         product = Product.objects.get(pk=pk)
         item_already_in_cart = False
         if request.session.has_key('phone'):
             phone = request.session['phone']
             total_item = len(Cart.objects.filter(phone=phone))
             item_already_in_cart = Cart.objects.filter(Q(product=product) & Q(phone=phone)).exists()
             customer = Customer.objects.filter(phone=phone)
             for c in customer:
                 name = c.name


             data = {
                 'product': product,
                 'item_already_in_cart': item_already_in_cart,
                 'name': name,
                 'total_item': total_item
             }
             return render(request, 'product-details.html', data)
    

def logout(request):
    if request.session.has_key('phone'):
        del request.session['phone']
        return redirect('login')
    else:
        return redirect('login')
    


def show_cart(request):
     total_item = 0
     if request.session.has_key('phone'):
             phone = request.session['phone']
             total_item = len(Cart.objects.filter(phone=phone))
             customer = Customer.objects.filter(phone=phone)
             
             for c in customer:
                 name = c.name

                 cart = Cart.objects.filter(phone=phone)
                 data = {
                     'cart': cart,
                     'name': name,
                     'total_item': total_item
                 }
                 if cart:
                     return render(request, 'show_cart.html', data)


