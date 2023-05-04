# View Page (Important Page For Django Page Display)
# It Consist of the Definations for Rendering Path Requested By user and Maintained By Developer


# Required Imports
from django.conf import settings 
from django.http import JsonResponse # Jssonresponse import fot JS Runnable ENV
from django.shortcuts import redirect, render # Rendering and redirecting Import by Django Shortcut
from django.views import View # importing Django View
import razorpay # Module razorpay import for payment
from .models import Cart, Customer, OrderPlaced, Payment, Product # Importing product Structure From Django.model(SELF created)
from . forms import CustomerRegistrationForm,CustomerProfileForm # Impoort registration form Django (inbuilt)
from django.contrib import messages # Importing messages lib from django (inbuilt)
from django.db.models import Q #logical Django lib



# import smtplib
# from smtplib import SMTP
from django.core.mail import send_mail
from django.conf import settings


def index1(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        # name = request.POST['name']
        send_mail(
            'Contact Form',
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )

    return render(request  , 'app/index1.html',locals())


# Home Page Rendering Defination
def home(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,"app/home.html",locals())



# Help Page Rendering Defination
def help(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,"app/help.html",locals())




# About Page Rendering Defination
def about(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,"app/about.html",locals())




# Logout Page Rendering Defination
def Logout(request):
    return render (request,"app/login.html",locals())




# Contact Page Rendering Defination
def contact(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,"app/contact.html",locals())




# (Blue-Print for Category View)
class CategoryView(View):
    # Get method to Fetch Data
    def get(self,request,val):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            product=Product.objects.filter(category=val)
            title=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())




# (Blue-Print for Product-Detail-View)
class ProductDetail(View):
    # Get Method to Fetch Data
    def get(self,request,pk):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            product=Product.objects.get(pk=pk)
        # wishlist=WislistModelAdmin.objects.filter(Q(product=product)&Q(user=request.user))
        # totalitem=0
        # if request.user.is_authenticated:
        #     totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,'app/productdetail.html' ,locals())




# (Blue-Print for Customer Registration-View)
class CustomerRegistrationView(View):
    # Get Method to Fetch data
    def get(self,request):
        # totalitem=0
        # if request.user.is_authenticated:
        #     totalitem=len(Cart.objects.filter(user=request.user))
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    


    # Form POST method to Get and Check the Inputs from User
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        # Check for Form Validation and Return Responses
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations User Registered Successfully")
        else:
            messages.warning(request,"Invalid Data Inputs")
        return render (request,'app/customerregistration.html',locals())
    



# (Blue-Print for Profile (Registration)-View)
class ProfileView(View):
    #cGet Method
    def get(self,request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            form = CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    
    # Post Method 
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        # Form Validations
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality =form.cleaned_data['locality']
            city =form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            # Profile Validations
            reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations,Profile Saved Succcessfully!!")
        else:
            messages.warning(request,"Invalid Data Inputs !!!")
        return render(request,'app/profile.html',locals())



# Address Page Rendering Defination
def address(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    add=Customer.objects.filter(user=request.user)
    return render (request,'app/address.html',locals())




# Add to cart Page Rendering Defination
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get("prod_id")
    product= Product.objects.get(id=product_id)
    Cart (user=user,products=product).save()
    return redirect("/cart")

 
# Show Cart Page Rendering Defination
def show_cart(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    user=request.user 
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity*p.products.discounted_price
        amount=amount+value
        totalamount=amount+40
    return render(request,'app/add_to_cart.html',locals())



# Serach Button Working and Rendering
def search(request):
    query=request.GET['search']
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    product= Product.objects.filter(Q(title__icontains=query))
    return render(request,"app/search.html",locals())



# Update Addresss View (Non Working)
class updateAddress(View):
    def get(request,pk):
        form=CustomerProfileForm()
        return render(request,'app/updateAddress.html',locals())
    def post(request,pk):
        form=CustomerProfileForm(request.POST)
        return render(request,'app/updateAddress.html',locals())
        


# Failing to Import JS File
def plus_cart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)&Q(user=request.user))
        c.quantity+=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        # print(prod_id)
        amount=0
        for p in cart:
            value=p.quantity*p.products.discounted_price
            amount=amount+value
        totalamount=amount+40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,

        }
        return JsonResponse(data)
    

# Method For Payment Done 
def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    user=request.user
    customer=Customer.objects.get(id=cust_id)
    payment=Payment.objects.get(razorpay_id=order_id)
    payment.paid=True
    payment.razorpay_payment_id=payment_id
    payment.save()
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
        c.delete()

    
    return redirect("cart")



# Orders Page Rendering Defination
def orders(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    opd=OrderPlaced.objects.filter(user=request.user)
    return render(request,"app/orders.html",locals())


# Chackek Out Class --> Extended To Payment Integration
class checkout(View):

    def get(self,request):
        totalitem=0
        totalitem=len(Cart.objects.filter(user=request.user))
        user=request.user

        add=Customer.objects.filter(user=user)
        cart=Cart.objects.filter(user=user)

        famount=0
        for p in cart:
            value=p.quantity*p.products.discounted_price
            famount=famount+value
        totalamount=famount+40
        razoramount=int(totalamount*100)

        client=razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data={"amount" :razoramount,"currency" :"INR","receipt":"order_rcptid_12"}
        payment_response=client.order.create(data=data)

        print(payment_response)

        order_id=payment_response['id']
        order_status=payment_response['status']

        if order_status=='created':
            payment=Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
        payment.save() 
        print('paymet is created')
        return render(request,'app/checkout.html',locals())
    

