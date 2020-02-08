from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '用户名', 'autofocus': True, 'required': True}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '密码', 'required': True}))


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '密码', 'required': True}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '确认密码', 'required': True}))

    class Meta:
        model = User
        fields = ['username', ]
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '用户名', 'autofocus': True, 'required': True}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('两次密码不一致！')
        return cd.get('password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
