from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='男', verbose_name='性别')
    mobile = models.CharField(max_length=11, default='', verbose_name='手机号码')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.user.username
