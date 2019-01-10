from django.contrib import admin

# Register your models here.
from .models import BillingProfile



class BillingProfileAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'active'
    ]




admin.site.register(BillingProfile,BillingProfileAdmin)

