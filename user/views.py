from django.shortcuts import render, redirect
from .form import LoginForm
from django.contrib import auth, messages
from django.contrib.auth.models import User


def login(request):
    next_url = request.GET.get('next', '/')
    login_button_disabled = True
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = auth.authenticate(username=cd.get('username'), password=cd.get('password'))
            if user:
                auth.login(request, user)
                return redirect(next_url)
            else:
                if User.objects.filter(username=cd.get('username')).exists():
                    messages.add_message(request, messages.ERROR, '密码错误！')
                else:
                    messages.add_message(request, messages.ERROR, '用户名不存在！')
                return render(request, 'user/login.html', locals())
        else:
            messages.add_message(request, messages.ERROR, '信息有误！')
            return render(request, 'user/login.html', locals())
    login_form = LoginForm()
    return render(request, 'user/login.html', locals())


def logout(request):
    next_url = request.GET.get('next', '/')
    auth.logout(request)
    return redirect(next_url)
