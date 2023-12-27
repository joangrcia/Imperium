from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):

    return render(request, 'base.html')

    # if request.method == 'GET':
    #     if request.user.is_authenticated:
    #         return redirect ('dashboard:index')
    #     else:
    #         return render(request, 'index.html')

    # if request.method == 'POST':
        
    #     username_login = request.POST.get('email')
    #     password_login = request.POST.get('password')

    #     user = authenticate(request, email=username_login, password=password_login)

    #     if user is not None:
    #         login(request, user)
    #         print("Login")
    #         return redirect('dashboard:index')
    #     else:
    #         messages.info(request, "Username or password incorrect.")
    #         print("Not Login")
    #         return redirect('login')