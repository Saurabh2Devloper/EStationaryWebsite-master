# Model Configuration For App

from django.db import models
from django.contrib.auth.models import User


# Model Created by Saurabh for Category Choices
CATEGORY_CHOICES={
    ('NB','NOTEBOOK'),
    ('DR','Dairy'),
    ('pn','Pens'),
    ('fl','files'),
    ('sc','scale'),
}



# Model Product Structure for our Stationaery Products 
class Product(models.Model):
    #Field for Title
    title=models.CharField(max_length=100)
    #Field for Selling Price
    selling_price=models.FloatField()
    #Field for Discounted Price
    discounted_price=models.FloatField()
    #Field for Product Discription
    description=models.TextField()
    #Field for Category Choice
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    #Field for Product image
    product_img=models.ImageField(upload_to='product')

    # Inbuild method to display Title on Page Site
    def __str__(self):
        return self.title


class Customer (models. Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models. CharField (max_length=200)
    locality = models. CharField (max_length=200)
    city =models. CharField(max_length=50)   
    mobile = models. CharField (max_length=10)
    zipcode = models. CharField(max_length=6)
    state = models. CharField ( max_length=100)
    def _str_(self):
        return self.name
    

class Cart (models. Model):
    user = models. ForeignKey (User, on_delete=models. CASCADE)
    products = models. ForeignKey (Product, on_delete=models. CASCADE)
    quantity = models. PositiveIntegerField (default=1)

    @property
    def total_cost (self):
          return self.quantity * self.product.discounted_price
    


class Payment (models. Model):  
    user = models. ForeignKey (User,on_delete=models.CASCADE)
    amount = models. FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True,null=True)
    razorpay_payment_status = models. CharField (max_length=100,blank=True, null=True)
    razorpay_payment_id = models. CharField (max_length=100, blank=True,null=True)
    paid = models. BooleanField (default=False)



STATUS_CHOICES={
    ('Accepted','Accepted'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
}


class OrderPlaced (models.Model):
    user = models. ForeignKey (User,on_delete=models. CASCADE)
    customer = models. ForeignKey (Customer, on_delete=models. CASCADE)
    product = models. ForeignKey (Product, on_delete=models. CASCADE)
    quantity = models. PositiveIntegerField (default=1)
    ordered_date= models.DateTimeField (auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models. ForeignKey (Payment, on_delete=models. CASCADE, default="")


@property
def totalcost (self):
    return self.quantity* self.product.discounted_price


class wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)