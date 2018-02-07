from django.db import models

# Create your models here.


class UserInfo(models.Model):
    u_name = models.CharField(max_length=20)
    u_pwd = models.CharField(max_length=40)
    u_email = models.CharField(max_length=30)


class UserAddress(models.Model):
    u_receive_name = models.CharField(max_length=20)
    u_receive_address = models.CharField(max_length=40)
    u_receive_number = models.CharField(max_length=6)
    u_receive_phone = models.CharField(max_length=11)
    u_user = models.ForeignKey('UserInfo')

