from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=500)
    father_name = models.CharField(max_length=500)
    customer_profile = models.CharField(max_length=500)
    loan_account_number = models.CharField(max_length=500)

class Branch(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zone_name = models.CharField(max_length=500)
    region_name = models.CharField(max_length=500)
    area_name = models.CharField(max_length=500)
    branch_name = models.CharField(max_length=500)
    branch_code = models.CharField(max_length=500)

class CustomerHomeAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    address3 = models.CharField(max_length=500)
    landmark = models.CharField(max_length=500)
    pincode = models.CharField(max_length=500)