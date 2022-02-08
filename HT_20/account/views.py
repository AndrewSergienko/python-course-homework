from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def account_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('shop:product_list')
            else:
                messages.error(request, 'Invalid login or password.')
        else:
            messages.error(request, 'Error. Try again or later.')
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}
    return render(request, 'account/login.html', context=context)


def account_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("shop:product_list")