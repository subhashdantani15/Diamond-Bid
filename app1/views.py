from django.shortcuts import render,redirect
from .form import UserRegisterForm
from .models import UserRegister,VendorRegister
# Create your views here.


def index(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'index.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'index.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'index.html')
    

def product(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'product.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'product.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'product.html')

def service(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'service.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'service.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'service.html')


def about(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'about.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'about.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'about.html')

def contact(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'contact.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'contact.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'contact.html')

def testimonial(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'testimonial.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'testimonial.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'testimonial.html')

def usersignup(request):
    obj=UserRegisterForm(request.POST) 
    if obj.is_valid():
        data=UserRegister.objects.all().filter(useremail=request.POST['useremail'])
        if len(data)<=0:
            obj.save()
            return redirect('userlogin')
        else:
            return render(request,'usersignup.html',{'messagekey':"User Already Exists"})
    return render(request,'usersignup.html')

def userlogin(request):
    if request.POST:
        email = request.POST['useremail']
        pass1 = request.POST['userpassword']
        try:
            valid = UserRegister.objects.get(useremail=email,userpassword=pass1)
            if valid:
                request.session['user'] = email
                request.session['userId'] = valid.pk
                return redirect('index')
            else:
                return render(request,'userlogin.html',{'messagekey':'Password incorrect'})
        except:
            return render(request,'userlogin.html',{'messagekey':'Password incorrect'})
    return render(request,'userlogin.html')

def logout(request):
    if 'user' in request.session.keys():
        del request.session['user']
        return redirect('userlogin')
    return redirect('userlogin')

def userchangepass(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'userchangepass.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'userchangepass.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'userchangepass.html')



def userprofile(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'userprofile.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'userprofile.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'userprofile.html')

def vendorlogin(request):
    if request.POST:
        email = request.POST['vendoremail']
        pass1 = request.POST['vendorpassword']
        try:
            valid = VendorRegister.objects.get(vendoremail=email,vendorpassword=pass1)
            if valid:
                request.session['vendor'] = email
                request.session['vendorId'] = valid.pk
                return redirect('index')
            else:
                return render(request,'vendorlogin.html',{'messagekey':'Password incorrect'})
        except:
            return render(request,'vendorlogin.html',{'messagekey':'Password incorrect'})
    return render(request,'vendorlogin.html')
def vendorlogout(request):
    if 'vendor' in request.session.keys():
        del request.session['vendor']
        return redirect('vendorlogin')
    return redirect('vendorlogin')
def vendorproduct(request):
    return render(request,'vendorproduct.html')