from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout')
]