from django.shortcuts import render,redirect
from .forms import GuestForm
from django.utils.http import is_safe_url

from django.views import View
from .models import GuestEmail

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)






class UserLoginView(View):
    """
    Description:Will be used to login and logout users.\n
    """
    template_name = ''
    def get(self,request,*args,**kwargs):
        form = 
        context = {
            "title":"Login",
            "form":form
        }
        return render(request,self.template_name,context)



