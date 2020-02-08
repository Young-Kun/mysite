import re

value = '<ul class="errorlist"><li>password2<ul class="errorlist"><li>两次密码不一致！</li></ul></li><li>username<ul class="errorlist"><li>已存在一位使用该名字的用户。</li></ul></li></ul>'
for message in re.findall(r'.<ul class="errorlist"><li>(.*?)</li></ul>', value):
    print(message)
