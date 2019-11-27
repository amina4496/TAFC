from __future__ import unicode_literals

from django.db import models

# Create your models here.

class keyvals(models.Model):
    pkv=models.CharField(max_length=400)
    msk=models.CharField(max_length=400)

class nots(models.Model):
    notif=models.CharField(max_length=4000)
class timeuser(models.Model):
    oruser=models.CharField(max_length=2000)
    anduser=models.CharField(max_length=2000)
    fid=models.IntegerField(default=0)
class stafc(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    cat=models.CharField(max_length=200)
    dob=models.CharField(max_length=200)
    dep=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    status=models.IntegerField(default=2)
    approve=models.IntegerField(default=0)
    role=models.CharField(max_length=200)
    sid=models.CharField(max_length=200,default="none")
    tid=models.CharField(max_length=200,default="none")
    sem=models.CharField(max_length=200,default="none")
class forfile(models.Model):
    priv=models.CharField(max_length=400)
    fid=models.IntegerField()
    filename=models.CharField(max_length=400)
class okay(models.Model):
    priv=models.CharField(max_length=400)
    fid=models.IntegerField()
    filename=models.CharField(max_length=400)
    username=models.CharField(max_length=400)
    uid=models.IntegerField()
class role(models.Model):
    department=models.CharField(max_length=200)
    drole=models.CharField(max_length=200)
    status=models.IntegerField(default=0)

class accepted(models.Model):
    uid=models.CharField(max_length=200)
    uname=models.CharField(max_length=200)
    role=models.CharField(max_length=200)

class rejected(models.Model):
    uid=models.CharField(max_length=200)
    uname=models.CharField(max_length=200)
    role=models.CharField(max_length=200)    

class askey(models.Model):
    uid=models.IntegerField(default=0)
    username=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    fileid=models.IntegerField(default=0)
    filename=models.CharField(max_length=200,default="none")
    status=models.IntegerField(default=0)


class filedates(models.Model):
    filename=models.CharField(max_length=500)
    access=models.CharField(max_length=500)
    time=models.CharField(max_length=500)
    date=models.CharField(max_length=500)
    approve=models.IntegerField(default=0)
    status=models.IntegerField(default=0)
    username=models.CharField(max_length=500,default="null")
