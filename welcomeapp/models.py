from django.db import models

# Create your models here.
class Visitors(models.Model):
    person_name = models.CharField(max_length=20, null=True)
    company = models.CharField(max_length=30, null=True)
    accompany = models.CharField(max_length=30, null=True) # 同伴者名
    person = models.IntegerField(null=True) # 同伴人数
    text1 = models.CharField(max_length=30, null=True)
    tantousya = models.CharField(max_length=30, null=True)# 担当者名
    dates = models.DateTimeField(null=True)# 日付
    affair1 = models.CharField(max_length=30,)#用件
    affair2 = models.CharField(max_length=30, null=True)#その他の用件


    #times=models.DateTimeField(auto_now_add=True, null=True)

    # entry_time = models.TimeField()
    # created = models.DateTimeField(auto_now_add=True, help_text='作成日')
    # modified = models.DateTimeField(auto_now=True, help_text='更新日')

    #visit_
    times=models.DateTimeField(auto_now_add=True, null=True)