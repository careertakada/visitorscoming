from django.db import models

from django.contrib.auth.models import User # ユーザー認証

# Create your models here.
class Visitors(models.Model):
    person_name = models.CharField(max_length=20, null=True)
    company = models.CharField(max_length=30, null=True)
    douhan = models.CharField(max_length=30, null=True) # 同伴者名
    douhan1 = models.CharField(max_length=30, null=True) # 同伴者名
    douhan2 = models.CharField(max_length=30, null=True) # 同伴者名
    person = models.IntegerField(null=True) # 同伴人数
    text1 = models.CharField(max_length=30, null=True)
    tantousya = models.CharField(max_length=30, null=True)# 担当者名
    dates = models.DateTimeField(null=True)# 日付
    affair1 = models.CharField(max_length=30,)#用件
    affair2 = models.CharField(max_length=30, null=True)#その他の用件

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)

def __str__(self):
        return self.user.username


    #times=models.DateTimeField(auto_now_add=True, null=True)

    # entry_time = models.TimeField()
    # created = models.DateTimeField(auto_now_add=True, help_text='作成日')
    # modified = models.DateTimeField(auto_now=True, help_text='更新日')

    #visit_
times=models.DateTimeField(auto_now_add=True, null=True)
