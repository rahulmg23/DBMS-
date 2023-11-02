from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name="about"),
    path('login/', views.loginPage, name="login"),
    path('signup/', views.Signup, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('vehicle/', views.vehiclePage, name="vehicle"),
    
   
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)