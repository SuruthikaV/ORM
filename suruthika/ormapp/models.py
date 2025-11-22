from django.db import models

# Create your models here.
from django.contrib import admin
class Product(models.Model):
    Name=models.CharField(max_length=100)
    Product_Id=models.CharField(max_length=10,primary_key=True)
    Brand_Name=models.CharField(max_length=30)
    Date_Of_Manufacture=models.DateField()
    Expire_Date=models.DateField()
    Price=models.FloatField()
    Stockavailable=models.IntegerField()
class ProductAdmin(admin.ModelAdmin):
    list_display=["Name","Product_Id","Brand_Name","Date_Of_Manufacture","Expire_Date","Price","Stockavailable"]