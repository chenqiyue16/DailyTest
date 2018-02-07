from django.shortcuts import render,redirect
from .models import UserInfo
from django.http import HttpResponse
from hashlib import sha1
import json
# Create your views here.


def register(request):
    return render(request, "df_user/register.html")


def checkUname(request):
    name = request.POST.get('name', None)
    rtxt=""
    name2 = UserInfo.objects.filter(u_name=name)
    if name2.exists():
        rtxt = "用户名已存在！"
        return HttpResponse(json.dumps({"msg": rtxt}))
    else:
        return HttpResponse()


def register_handle(request):
    u_name = request.POST.get('inputUser')
    u_pwd = request.POST.get('inputPassword')
    u_email = request.POST.get('inputEmail')
    print(u_name)
    print(u_email)
    print(u_pwd)
    s1 = sha1()
    s1.update(u_pwd.encode("utf8"))
    upwd_hash = s1.hexdigest()

    user = UserInfo()
    user.u_name = u_name
    user.u_pwd = upwd_hash
    user.u_email = u_email
    user.save()
    return redirect('/user/login')


def login(request):
    return render(request, 'df_user/login.html')