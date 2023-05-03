from django.urls import path
from app1.views import *

urlpatterns = [
    path('', index,name='index'),
    path('product/', product,name='product'),
    path('service/', service,name='service'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('testimonial/', testimonial,name='testimonial'),
    path('usersignup/', usersignup,name='usersignup'),
    path('userlogin/', userlogin,name='userlogin'),
    path('userchangepass/', userchangepass,name='userchangepass'),
    path('userprofile/', userprofile,name='userprofile'),
    path('vendorlogin/', vendorlogin,name='vendorlogin'),
    path('vendorproduct/', vendorproduct,name='vendorproduct'),
    path('logout/',logout,name='logout'),
    path('vendorlogout/',vendorlogout,name='vendorlogout')



   
]