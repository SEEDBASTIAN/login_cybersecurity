from django.urls import path
from .views import login_view, home_view

from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

