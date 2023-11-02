from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
             'type':'text',
             'name':'username',
             'placeholder':'Username', 
             'class':'box',
             'required':''
        })

        self.fields['email'].widget.attrs.update({
             'type':'email',
             'name':'email',
             'placeholder':'Email', 
             'class':'box',
             'required':''
        })

        self.fields['password1'].widget.attrs.update({
             'type':'password',
             'name':'password1',
             'placeholder':'Password', 
             'class':'box',
             'required':''
        })

        self.fields['password2'].widget.attrs.update({
             'type':'password',
             'name':'password2',
             'placeholder':'Confirm Password', 
             'class':'box',
             'required':''
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ContactForm(ModelForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
             'type':'text',
             'name':'first_name',
             'placeholder':'First Name', 
             'class':'box',
             'required':''
        })

        self.fields['last_name'].widget.attrs.update({
             'type':'text',
             'name':'last_name',
             'placeholder':'Last Name', 
             'class':'box',
             'required':''
        })

        self.fields['gender'].widget.attrs.update({
             'type': 'text',
             'name':'first_name',
             'placeholder':'First Name', 
             'class':'box',
             'required':''
        })

        self.fields['email'].widget.attrs.update({
             'type': 'text',
             'name':'email',
             'placeholder':'Email', 
             'class':'box',
             'required':''
        })

        self.fields['contact'].widget.attrs.update({
             'type': 'text',
             'name':'contact',
             'placeholder':'Contact', 
             'class':'box',
             'required':''
        })

        self.fields['city'].widget.attrs.update({
             'type': 'text',
             'name':'city',
             'placeholder':'City', 
             'class':'box',
             'required':''
        })

        self.fields['state'].widget.attrs.update({
             'type': 'text',
             'name':'state',
             'placeholder':'State', 
             'class':'box',
             'required':''
        })

        self.fields['address'].widget.attrs.update({
             'type': 'text',
             'name':'address',
             'placeholder':'Address', 
             'class':'box',
             'required':''
        })



     class Meta:
          model = Customer
          fields = ['first_name', 'last_name','gender', 'email', 'contact', 'city', 'state', 'address' ]