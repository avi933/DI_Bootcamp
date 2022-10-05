from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number =models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__ (self):
        return f'{self.first_name} {self.last_name}'


class Vehicle_Type(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f' {self.name}'

class Vehicle_Size(models.Model):
    name = models.CharField(max_length= 100)
    
    def __str__(self):
        return f' {self.name}'

class Vehicle(models.Model):
    date_created = models.DateField()
    real_cost = models.CharField(max_length=20)
    size = models.CharField(max_length= 20)
    vehicle_type = models.ForeignKey('Vehicle_Type',on_delete=models.CASCADE,)
    size = models.ForeignKey('Vehicle_Size',on_delete=models.CASCADE,)
    def __str__(self):
        return f' {self.size} {self.vehicle_type}'


class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE) 
    vehicle = models.ForeignKey('Vehicle',on_delete=models.CASCADE)


class Rental_Rate(models.Model):
    daily_rate = models.CharField(max_length=20)
    vehicle_type = models.ForeignKey('Vehicle_Type',on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey('Vehicle_Size',on_delete=models.CASCADE) 