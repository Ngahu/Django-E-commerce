from django.shortcuts import render,redirect
from .forms import GuestForm
from django.utils.http import is_safe_url

from django.views.generic import CreateView
from django.views import View

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .models import GuestEmail
from .forms import UserLoginForm,UserRegisterForm





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
        form = UserLoginForm(request.POST or None)

        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email,password=password)

            if user is not None:
                login(request,user)

                if is_safe_url(redirect_path,request.get_host()):
                    return redirect(redirect_path)
                
                else:
                    return redirect("/")
            
            else:
                print("error")

        
        context = {
            "title":"Login",
            "form":form
        }
        return render(request,self.template_name,context)






# class RegisterView(CreateView):
#     form_class = UserRegisterForm
#     template_name = 'accounts/register.html'
#     success_url = '/login/'







class RegisterView(View):
    """
    Description:View to create a new user.\n
    """
    template_name = 'accounts/register.html'
    
    def get(self,request,*args,**kwargs):
        form = UserRegisterForm()
        context = {
            "title":"Register",
            "form":form
        }
        return render(request,self.template_name,context)

    
    def post(self,request,*args,**kwargs):
        form = UserRegisterForm(request.POST or None)
        next_ = request.GET.get('next')

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            
            login(request, user)
            if next_:
                return redirect(next_)
            return redirect("/")

    
        context = {
            "title":"Register",
            "form":form
        }
        return render(request,self.template_name,context)

