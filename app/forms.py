# Form Control Page (forms.py)

# Imports from Djano (Ease Imports-Inbuilt)
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User # To import activity by user
from .models import Customer

class LoginForm (AuthenticationForm):
        username = UsernameField (widget=forms.TextInput 
                                 (attrs={'autofocus ': 'True',
                                'class': 'form-control'}))
        password = forms.CharField (widget=forms.PasswordInput (attrs=
                                    {'autocomplete': 'current-password', 
                                    'class': 'form-control'}))

# Customer Registration Template
class CustomerRegistrationForm(UserCreationForm): # Inheritance !!!! For userfield
    # Fields Required in Form
    username = forms.CharField(widget=forms.TextInput # type of input : TEXTAREA FIELD
                            #    (# Widget == Prestructured Field By Django Inbuilt)
                                (attrs={
                                # Attributes Provided By Form Lib import
                                'autofocus ': 'True', # On Page start Cursor chi Jaga
                                'class': 'form-control' # Internal Django Form Control
                                }))
    

    email = forms.EmailField(widget=forms.EmailInput  # type of input : EMAIL FIELD
                                (attrs={ # Attributes
                                'class': 'form-control'# Internal Django Form Control
                                 }))
    

    password1 = forms.CharField(label='Password', # TO label the field (just like placeholder)
                                widget=forms.PasswordInput  # type of input : PASSWORD FIELD
                                (attrs={ # Attributes
                                'class': 'form-control'# Internal Django Form Control
                                }))
    

    password2 = forms.CharField(label='Confirm Password', # TO label the field (just like placeholder)
                                widget=forms.PasswordInput
                                (attrs={ # Attributes
                                'class': 'form-control'# Internal Django Form Control
                                }))
    
    # Short Form Model For Takeup Field Reponses filled by user
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class MyPasswordResetForm(PasswordChangeForm):
    pass





class CustomerProfileForm(forms.ModelForm):
     class Meta:
          model =Customer
          fields=['user','name','locality','city','mobile','state','zipcode']
          widgets={
            'name': forms.TextInput (attrs= { 'class': 'form-control' }),
            'locality': forms.TextInput (attrs={'class': 'form-control' }), 
            'city': forms.TextInput (attrs={'class': 'form-control'}),
            'mobile': forms. NumberInput (attrs={'class': 'form-control' }),
            'state': forms.TextInput (attrs={'class': 'form-control'}),
            'zipcode': forms. NumberInput (attrs= { 'class': 'form-control' }),
}

