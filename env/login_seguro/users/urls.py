from django.urls import path
from .views import SecureLoginView

urlpatterns = [
    path('login/', SecureLoginView.as_view(), name='login'),
]
