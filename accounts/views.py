from django.shortcuts import render,redirect
from .forms import GuestForm
from django.utils.http import is_safe_url

from django.views import View

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .models import GuestEmail
from .forms import UserLoginForm





class UserLoginView(View):
    """
    Description:Will be used to login and logout users.\n
    """
    template_name = 'accounts/login.html'
    def get(self,request,*args,**kwargs):
        form = UserLoginForm()
        context = {
            "title":"Login",
            "form":form
        }
        return render(request,self.template_name,context)

    

    def post(self,request,*args,**kwargs):
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email,password=password)
            login(request,user)
            if next:
                return redirect(next)
            
            return redirect("/")
        
        
        context = {
            "title":"Login",
            "form":form
        }
        return render(request,self.template_name,context)



