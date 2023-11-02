from email.headerregistry import Address
from re import A
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICE = [('Active', 'Active'),('Inactive', 'Inactive')]


class Dealer(models.Model):
    dealer_id = models.IntegerField(primary_key=True, unique=True)
    dealer_img = models.ImageField(blank=False)
    dealer_name = models.CharField(max_length=100, blank=False, null=False)
    dealer_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='d_username')
    last_login = models.DateTimeField(auto_now=True)
    contact = models.IntegerField(null=False, blank=False)
    company_name = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(max_length=300, blank=False, null=False)
    created = models.DateTimeField(auto_created=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default= 'Active')

    def __str__(self):
       return str(self.dealer_id)

VEHICLE_TYPE = [
    ("Hatchback", "Hatchback"),
    ("Sedan", "Sedan"),
    ("MPV", "MPV"),
    ("SUV", "SUV"),
    ("Crossover", "Crossover"),
    ("Coupe", "Coupe"),
    ("Convertible", "Convertible")
]

VEH_STATUS = [
    ("For Sale", "For Sale"),
    ("Sold", "Sold")
]

class Vehicle(models.Model):
    vehicle_id = models.IntegerField(primary_key=True, unique=True)
    dealer_id = models.ForeignKey(Dealer, to_field='dealer_id', on_delete=models.CASCADE)
    vehicle_img = models.ImageField(blank=False)
    name = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=100, choices=VEHICLE_TYPE, blank=False)
    description = models.TextField(max_length=100, blank=False)
    cost = models.IntegerField(blank=False)
    status = models.CharField(max_length=20, choices=VEH_STATUS, blank=False, default='For Sale')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
]

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=100, blank=False, choices=GENDER)
    email = models.CharField(max_length=100, blank=False)
    contact = models.IntegerField(blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    address = models.TextField(max_length=100, blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

SALE_STATUS = [
    ("Sold", "Sold"),
    ("On hold", "On hold"),
    ("Rejected", "Rejected")
]

class Sale(models.Model):
    customer_id = models.ForeignKey(Customer, to_field='customer_id', on_delete=models.CASCADE)
    sale_id = models.IntegerField(primary_key=True, unique=True)
    vehicle_id = models.ForeignKey(Vehicle, to_field='vehicle_id', on_delete=models.CASCADE)
    description = models.TextField(max_length=100, blank=False)
    order_date = models.DateTimeField(auto_created=True)
    cost = models.IntegerField(blank=False)
    deal_date = models.DateTimeField(auto_created=True)
    status = models.CharField(max_length=20, blank=False, choices=SALE_STATUS)
    tax_id = models.IntegerField(unique=True, blank=False)
    
    def __str__(self):
        return str(self.vehicle_id)

TAX_STATUS = [ 
    ("Approved", "Approved"),
    ("Pending", "Pending"),
    ("Rejected", "Rejected")
]

class Tax(models.Model):
    tax_id = models.ForeignKey(Sale, to_field='tax_id', on_delete=models.CASCADE)
    tax = models.IntegerField(blank=False)
    description = models.TextField(max_length=100, blank=False)
    status = models.CharField(max_length=20, blank=False, choices=TAX_STATUS)

    def __str__(self):
        return str(self.tax_id)
