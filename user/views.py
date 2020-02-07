from django.shortcuts import render, redirect
from .form import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    next_url = request.GET.get('next', '/')
    login_button_disabled = True
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd.get('username'), password=cd.get('password'))
            if user:
                login(request, user)
                return redirect(next_url)
            else:
                messages.add_message(request, messages.ERROR, '用户名或密码错误！')
                return render(request, 'user/login.html', locals())
        else:
            messages.add_message(request, messages.ERROR, '信息有误！')
            return render(request, 'user/login.html', locals())
    login_form = LoginForm()
    return render(request, 'user/login.html', locals())


def user_logout(request):
    logout(request)
    return redirect('blog:index')
