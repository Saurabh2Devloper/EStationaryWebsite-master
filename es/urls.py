# URL Configuration

# In a Django project,
# urls.py is a Python module that contains the URL configuration for the project.
# It is responsible for mapping URLs to view functions,
# Written under views.py of Project


# Necessory imports
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


# URL Patterns for Page Configuration
urlpatterns = [
    # Administartion path
    path('admin/', admin.site.urls),
    # Home Page View (Default path for 'http://127.0.0.1:8000')
    path('',include("app.urls")),
    # Path to About Page for site
    path('about/',include("app.urls")),
    # Path to Contact Page for site
    path('contact/',include("app.urls")),
    # path('accounts/login/',auth_view.LoginView.as_View(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    # path('password-reset/',auth_view.PasswordResetView.as_View(template_name='app/password_reset.html',form=MyPasswordResetForm),name='password_reset'),

    

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# Path for Media (Images Display Directly Fetched from Media Directory) Static 
    
    
