from django.db import models
import datetime
# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    height = models.IntegerField()
    weight = models.IntegerField()
    quote = models.CharField(max_length=32)
    userid = models.IntegerField(primary_key=True, auto_created=True)
    #inittime = models.DateTimeField()
    croutine = models.ForeignKey(
        to='Routine', on_delete=models.CASCADE, null=True)
    croutine_starttime = models.DateTimeField(null=True)


class PostInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=160)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)


class KeyWord(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    users = models.ManyToManyField(to='UserInfo')
    keyword = models.CharField(max_length=12)


class Routine(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    routine = models.CharField(max_length=12)
    users = models.ManyToManyField(to='UserInfo', null=True)


class SpecialEvent(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    routine = models.CharField(max_length=12)
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)


class RoutineRecord(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    routine = models.ForeignKey(to='Routine', on_delete=models.CASCADE)
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    starttime = models.DateTimeField(auto_now=False, auto_now_add=False)
    endtime = models.DateTimeField(auto_now=False, auto_now_add=False)
    manualend = models.BooleanField()
