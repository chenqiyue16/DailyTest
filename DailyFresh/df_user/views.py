from django.shortcuts import render,redirect
from .models import UserInfo
from django.http import HttpResponse,HttpResponseRedirect
from hashlib import sha1
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def register(request):
    return render(request, "df_user/register.html")


@csrf_exempt
def checkUname(request):
    name = request.POST.get('name', None)
    rtxt=""
    name2 = UserInfo.objects.filter(u_name=name)
    if name2.exists():
        rtxt = "用户名已存在！"
        return HttpResponse(json.dumps({"msg": rtxt}))
    else:
        return HttpResponse(json.dumps({"msg": rtxt}))

@csrf_exempt
def checkPwd(request):
    name = request.POST.get('name', None)
    pwd = request.POST.get('pwd', None)

    s1 = sha1()
    s1.update(pwd.encode("utf8"))
    upwd_hash = s1.hexdigest()
    pwd2 = UserInfo.objects.filter(u_name=name, u_pwd=upwd_hash)
    if pwd2.exists():
        rtxt = "登录成功！"
        return HttpResponse(json.dumps({"msg": rtxt}))
    else:
        rtxt = "密码错误！"
        return HttpResponse(json.dumps({"msg": rtxt}))


def register_handle(request):
    u_name = request.POST.get('inputUser')
    u_pwd = request.POST.get('inputPassword')
    u_email = request.POST.get('inputEmail')

    s1 = sha1()
    s1.update(u_pwd.encode("utf8"))
    upwd_hash = s1.hexdigest()

    user = UserInfo()
    user.u_name = u_name
    user.u_pwd = upwd_hash
    user.u_email = u_email
    user.save()
    return redirect('/user/login/')

@csrf_exempt
def login_handle(request):
    u_name = request.POST.get('LoginInputUser')
    u_pwd = request.POST.get('LoginInputPassword')
    u_check = request.POST.get('checkout', 0)
    print("uname::"+u_name)
    s1 = sha1()
    s1.update(u_pwd.encode("utf8"))
    upwd_hash = s1.hexdigest()
    name = UserInfo.objects.filter(u_name=u_name)
    pwd = UserInfo.objects.filter(u_name=u_name, u_pwd=upwd_hash)
    if name.exists():
        if pwd.exists():
            red = HttpResponseRedirect('/user/user_center_info/')
            if u_check == 1:
                red.set_cookie('u_name', u_name)
            else:
                red.set_cookie('u_name', '', max_age=-1)
            request.session['u_name'] = u_name
            request.session['u_id'] = name[0].id
            return red
        else:
            context = {'error_name': 0, 'error_password': 1}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'error_name': 1, 'error_password': 0}
        return render(request, 'df_user/login.html', context)


def login(request):
    return render(request, 'df_user/login.html')


def user_center_info(request):
    context={}
    u_session = request.session.get('u_name')
    u_id = request.session.get('u_id')
    if u_session != "":
        context = {'u_name': u_session, 'u_id': u_id}
    print('u_session'+u_session+':::'+str(u_id))
    return render(request, 'df_user/user_center_info.html', context)