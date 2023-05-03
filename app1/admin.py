from django.contrib import admin
from .models import UserRegister,VendorRegister
# Register your models here.
class userregister(admin.ModelAdmin):
    list_display=['username','useremail','usercontactno','usergender','user_DOB',]

admin.site.register(UserRegister,userregister)

class vendorregister(admin.ModelAdmin):
    list_display=['vendorname','vendoremail','vendorcontactno','company_address','vendor_GST_no',]

admin.site.register(VendorRegister,vendorregister)