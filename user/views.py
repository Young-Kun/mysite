from django.shortcuts import render, redirect
from .form import LoginForm, RegistrationForm
from .models import UserProfile
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    next_url = request.GET.get('next', '/blog/index')
    register_login_button_disabled = 'disabled'
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
            messages.add_message(request, messages.ERROR, login_form.errors)
            return render(request, 'user/login.html', locals())
    login_form = LoginForm()
    return render(request, 'user/login.html', locals())


def logout(request):
    next_url = request.GET.get('next', '/blog/index')
    auth.logout(request)
    return redirect(next_url)


def register(request):
    next_url = request.GET.get('next', '/blog/index')
    register_login_button_disabled = 'disabled'
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data.get('password'))
            new_user.save()
            messages.add_message(request, messages.SUCCESS, '注册成功！您可以<strong>登录</strong>了！')
            return redirect('/user/login/?next=' + next_url)
        else:
            messages.add_message(request, messages.ERROR, register_form.errors)
            return render(request, 'user/register.html', locals())
    register_form = RegistrationForm()
    return render(request, 'user/register.html', locals())


@login_required
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user) if \
        hasattr(request.user, 'userprofile') \
        else UserProfile.objects.create(user=request.user)
    return render(request, 'user/profile.html', locals())


