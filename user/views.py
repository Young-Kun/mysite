from django.shortcuts import render, redirect
from .form import LoginForm, RegistrationForm, UserForm, UserProfileForm
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
    user_profile = UserProfile.objects.get(user=request.user) if \
        hasattr(request.user, 'userprofile') \
        else UserProfile.objects.create(user=request.user)
    return render(request, 'user/profile.html', locals())


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user) if \
        hasattr(request.user, 'userprofile') \
        else UserProfile.objects.create(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * user_profile_form.is_valid():
            user_cd = user_form.cleaned_data
            user_profile_cd = user_profile_form.cleaned_data
            request.user.email = user_cd.get('email')
            request.user.first_name = user_cd.get('first_name')
            user_profile.tags = user_profile_cd.get('tags')
            user_profile.gender = user_profile_cd.get('gender')
            user_profile.birth = user_profile_cd.get('birth')
            user_profile.mobile = user_profile_cd.get('mobile')
            user_profile.address = user_profile_cd.get('address')
            request.user.save()
            user_profile.save()
            messages.add_message(request, messages.SUCCESS, '修改成功！')
            return redirect('user:profile')
        else:
            messages.add_message(request, messages.ERROR, user_form.errors)
            messages.add_message(request, messages.ERROR, user_profile_form.errors)
            return render(request, 'user/edit_profile.html', locals())
    user_form = UserForm(instance=request.user)
    user_profile_form = UserProfileForm(instance=user_profile)
    return render(request, 'user/edit_profile.html', locals())
