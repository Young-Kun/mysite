# Generated by Django 3.0.2 on 2020-02-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200208_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码'),
        ),
    ]
