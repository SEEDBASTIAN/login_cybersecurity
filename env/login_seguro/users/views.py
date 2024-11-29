from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import SecureLoginForm

class SecureLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = SecureLoginForm

    @method_decorator(login_required)
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
