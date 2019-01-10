from django.conf.urls import url

from .views import (
    UserLoginView,
    RegisterView
)



urlpatterns = [
    url(r'^login/$',UserLoginView.as_view(),name='user_login'),
    url(r'^register/$',RegisterView.as_view(),name='user_register'),
]