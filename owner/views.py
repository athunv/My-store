from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from owner.forms import LoginForm,Registrationform,Productform
from django.contrib.auth.models import User

class Homeview(View):

    def get(self,request,*args,**kw):

        return render(request,"home.html") 
    
class Signupview(View):

    def get(self,request,*args,**kw):

        form = Registrationform

        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kw):

        form = Registrationform(request.POST)
        form1 = LoginForm()

        if form.is_valid():

            # form.save()
            User.objects.create_user(**form.cleaned_data)
            return render(request,"login.html",{"form":form1})
        else:
            return render(request,"register.html",{"form1":form})

    
class SigninView(View):

    def get(self,request,*args,**kw):

        form = LoginForm
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kw):
        
        print(request.POST)             #['username': 'athun' 'password' : 'hgaf' ] 
        print(request.POST.get("username"))
        print(request.POST.get("username"))

        return render(request,"home.html")
    
class ProductAddview(View):

    def get(self,request,*args,**kw):

        form = Productform

        return render(request,"product_add.html",{"form":form})
    
    def post(self,request,*args,**kw):

        form = Productform(request.POST ,files=request.FILES)

        if form.is_valid():
            form.save()
            return render(request,"home.html",{"form":form})

        else:
            return render(request,"product_add.html",{"form":form})