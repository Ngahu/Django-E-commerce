from django.contrib import admin

# Register your models here.
from .models import ObjectViewed,UserSession


class ObjectViewedAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'timestamp'
    ]



admin.site.register(ObjectViewed,ObjectViewedAdmin)



class UserSessionAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'session_key',
        'active',
        'timestamp'
    ]



admin.site.register(UserSession,UserSessionAdmin)

