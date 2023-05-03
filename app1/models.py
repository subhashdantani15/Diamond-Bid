from django.db import models

# Create your models here.
class UserRegister(models.Model):
    username=models.CharField(max_length=20,default='',verbose_name='User Name')
    useremail=models.EmailField(max_length=50,verbose_name='Email')
    usercontactno=models.IntegerField(default='',verbose_name='Contact No')
    g = [
        (None, 'select gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    usergender=models.CharField(max_length=12,choices=g,default=None)
    user_DOB=models.DateField()
    user_address=models.TextField()
    userpassword=models.CharField(max_length=20,verbose_name='Password')
    
    def __str__(self):
        return self.username

class VendorRegister(models.Model):
    vendorname=models.CharField(max_length=20,default='',verbose_name='Vendor Name')
    vendoremail=models.EmailField(max_length=50,verbose_name='Email')
    vendorcontactno=models.IntegerField(default='',verbose_name='Contact No')
    company_address=models.TextField()
    vendorpassword=models.CharField(max_length=20,verbose_name='Password')
    vendor_GST_no=models.CharField(max_length=50,verbose_name='Vendor GST No')
    
    def __str__(self):
        return self.vendorname