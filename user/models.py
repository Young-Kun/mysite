from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='用户')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='男', verbose_name='性别')
    birth = models.DateField(blank=True, null=True, verbose_name='出生日期')
    mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name='手机号码')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='地址')
    tags = models.CharField(max_length=255, blank=True, null=True, verbose_name='标签')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.user.username
