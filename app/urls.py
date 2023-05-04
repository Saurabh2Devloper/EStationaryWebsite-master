# URL Configuration Pgae

# Ways TO Import URLS
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))




# Neccesory Imports
from django.urls import path # importing path url
from . import views # importing views
from django.conf import settings # importing settings.py via django config method
from django.conf.urls.static import static # importing static directory
from django.contrib.auth import views as auth_view #authentication View
from .forms import MyPasswordResetForm,LoginForm # LoginformImport

# import smtplib


# URL Patterns path declarations
urlpatterns = [
    # Home path
    path('', views.home , name='home'),
    path('index1/' , views.index1 , name="index1"),
    # About Path
    path('help/', views.help,name="help"),
    path('about/', views.about,name="about"),
    # Conatct path
    path('contact/', views.contact,name='contact'),
    # Category path
    path('category/<slug:val>',views.CategoryView.as_view(),name="category"),
    # Product Detail Path
    path('product-detail/<int:pk>',views.ProductDetail.as_view(),name="product-detail"),
    #login Authentication
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    #login path
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    #logout path
    path('logout/',views.Logout,name='logout'),
    #profile path
    path('profile/',views.ProfileView.as_view(),name='profile'),
    #address path
    path('address/',views.address,name='address'),
    #address redirection login path
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name="login"),
    #path updateaddress
    path('contact/updateAddress/<int:pk>',views.updateAddress.as_view(),name="updateaddress"),
    #addtocart path
    path('add-to-cart/',views.add_to_cart,name="add-to-cart"),
    #cart path
    path('cart/',views.show_cart,name="showcart"),
    #chackout page
    path('checkout/',views.checkout.as_view(),name="checkout"),
    #searchbtn path
    path('search',views.search,name="search"),
    #plus cart btn
    path('plus-cart/',views.plus_cart),
    #paymentdone path
    path('paymentdone/',views.payment_done,name="paymentdone"),
    #orders on home page path
    path('orders/',views.orders,name="orders"),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# Static img diplay / media import 

