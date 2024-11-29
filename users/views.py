from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, 'login.html')


from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'users/home.html')