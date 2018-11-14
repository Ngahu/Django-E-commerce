from django.shortcuts import render,redirect
from .forms import GuestForm
from django.utils.http import is_safe_url
# Create your views here.

from .models import GuestEmail
