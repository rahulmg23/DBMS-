from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ContactForm
from .models import Vehicle

# Create your views here.



def Home(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'index.html', context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist!')

    
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')

def About(request):    
    return render(request, 'about.html')

def Signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User not created!')

    return render(request, 'signup.html', {'form':form})

def vehiclePage(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles':vehicles}
    return render(request, 'vehicles.html', context)

