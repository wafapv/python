from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Adminprofile(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=6)
    dist=models.CharField(max_length=100)
    photo=models.CharField(max_length=500)

class Product(models.Model):
    productname=models.CharField(max_length=100)
    price=models.IntegerField()
    photo1=models.CharField(max_length=500)
    photo2=models.CharField(max_length=500)

class User(models.Model):
     name=models.CharField(max_length=100)
     phoneno=models.CharField(max_length=10)
     email=models.CharField(max_length=100)
     houseno=models.CharField(max_length=100)
     place=models.CharField(max_length=100)
     post=models.CharField(max_length=100)
     pin=models.CharField(max_length=6)
     dist=models.CharField(max_length=100)
     LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)



class Order(models.Model):
    date=models.DateField()
    date2=models.DateField()
    status=models.CharField(max_length=100)
    paystatus=models.CharField(max_length=100)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)


class Complaint(models.Model):
    date=models.DateField()
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)


class Review(models.Model):
    date=models.DateField()
    review=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)


class Payment(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE)
    amount=models.FloatField()
    date=models.DateField()
    status=models.CharField(max_length=100)

class customisationrequest(models.Model):
    date=models.DateField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    description=models.CharField(max_length=1000)
    status=models.CharField(max_length=100)
    paystatus=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    reference=models.CharField(max_length=500)


class CustomPayment(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    CUSTOMREQUEST=models.ForeignKey(customisationrequest,on_delete=models.CASCADE)
    amount=models.FloatField()
    date=models.DateField()
    status=models.CharField(max_length=100)
