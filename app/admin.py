# Pannel For administration Contrls

# Requied Imports
from django.contrib import admin
from . models import Cart, OrderPlaced, Payment, Product,Customer, wishlist
# (Here . Represents the Current Directory)


# Module Registration for Product on Admin Site
@admin.register(Product)
# Python Class For Product (Admin)
class ProductModelAdmin(admin.ModelAdmin):
    # Disply list
    list_display=['id','title','discounted_price','category','product_img']
    # Admin Can Edit the Products to Display on E Stationaery Site
    # This is Entirely handled By Admin For Product Registration (Adding or Removing or Editing)



@admin.register(Customer)
class CutomerModelAdmin(admin.ModelAdmin):
    list_display=['user','locality','city','mobile','zipcode','state']



@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','products','quantity']
    


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status','paid']



@admin.register(OrderPlaced)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']



@admin.register(wishlist)
class WislistModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product']

