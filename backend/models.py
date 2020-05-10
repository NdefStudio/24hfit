from django.db import models

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
    inittime = models.DateTimeField()


class PostInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(to=UserInfo, on_delete=models.CASCADE)
    content = models.CharField(max_length=160)
    time = models.TimeField(auto_now=False, auto_now_add=False)


class KeyWord(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    users = models.ManyToManyField(to=UserInfo)
    keyword = models.CharField(max_length=6)


class Routine(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    routine = models.CharField(max_length=6)
    users = models.ManyToManyField(to=UserInfo)


class SpecialEvent(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    routine = models.CharField(max_length=6)
    user = models.ForeignKey(to=UserInfo, on_delete=models.CASCADE)


class RoutineRecord(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    routine = models.ForeignKey(to=Routine, on_delete=models.CASCADE)
    starttime = models.DateTimeField(auto_now=False, auto_now_add=False)
    endtime = models.DateTimeField(auto_now=False, auto_now_add=False)
    manualend = models.BooleanField()
