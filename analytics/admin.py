from django.contrib import admin

# Register your models here.
from .models import ObjectViewed,UserSession


admin.site.register(ObjectViewed)
admin.site.register(UserSession)

