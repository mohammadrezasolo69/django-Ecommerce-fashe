from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from ecommerce_user.models import User
from .forms import LoginUserForm, RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login is successfully', 'success')
                return redirect('product:home')
    else:
        form = LoginUserForm()
    return render(request, 'account/login.html', context={'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'logout is successfully', 'success')
    return redirect('product:home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = User.objects.create_user(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                email=cd['email'],
                password=cd['password1']
            )
            new_user.save()
            messages.success(request,'you registered successfully', 'success')
            login(request, new_user)
            return redirect('/')

    else:
        form = RegisterUserForm()
    return render(request, 'account/register.html', context={'form':form})
