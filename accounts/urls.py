from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from .views import (
    UserLoginView,
    RegisterView,
    guest_user_view
)



urlpatterns = [
    url(r'^login/$',UserLoginView.as_view(),name='user_login'),
    url(r'^register/$',RegisterView.as_view(),name='user_register'),
    url(r'^logout/$',LogoutView.as_view(),name='user_logout'),    
    url(r'^guest-user/$',guest_user_view,name='guest_user_register'),    
]