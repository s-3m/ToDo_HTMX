import django.contrib.auth.urls
from django.urls import path, include
from main.views import LoginUser, logout_user

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]