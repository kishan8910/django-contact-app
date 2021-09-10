from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=500)
    father_name = models.CharField(max_length=500, null=True)
    customer_profile = models.CharField(max_length=500, null=True)
    loan_account_number = models.CharField(max_length=500, null=True)


class Branch(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zone_name = models.CharField(max_length=500, null=True)
    region_name = models.CharField(max_length=500, null=True)
    area_name = models.CharField(max_length=500, null=True)
    branch_name = models.CharField(max_length=500, null=True)
    branch_code = models.CharField(max_length=500, null=True)


class CustomerHomeAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=500, null=True)
    address2 = models.CharField(max_length=500, null=True)
    address3 = models.CharField(max_length=500, null=True)
    landmark = models.CharField(max_length=500, null=True)
    pincode = models.CharField(max_length=500, null=True)
