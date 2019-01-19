from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def register_views(request):
    if request.method == 'GET':
        #使用自定义form类
        # form = RegisterForm()
        #使用与models相关联的form类
        form = ModelRegisterForm()
        return render(request,'00-post.html',locals())
    else:
        #1.将register.POST给RegisterForm()
        # form = RegisterForm(request.POST)

        #将request.POST给ModelRegisterForm()
        form = ModelRegisterForm(request.POST)

        #2.判断是否通过验证
        if form.is_valid():
        #3验证通过后,获取数据构建成Users的对象
            user = Users(**form.cleaned_data)
        #4.将Users的对象保存会数据库
            user.save()
            return HttpResponse('注册成功')
        return HttpResponse('数据有误,注册失败')

def login_views(request):
    if request.method == 'GET':
        form = ModelLoginFrom()
        return render(request,'01-login.html',locals())
    else:
        # form = ModelLoginFrom(request.POST)
        # if form.is_valid():
        #     uname = form.cleaned_data.get('uname')
        #     upwd = form.cleaned_data.get('upwd')
        #
        #     if Users.objects.filter(uname=uname) and Users.objects.filter(upwd=upwd):
        #
        #         return HttpResponse('登录成功')
        #
        #     return HttpResponse('用户名密码错误')

        uname = request.POST['uname']
        upwd = request.POST['upwd']
        users = Users.objects.filter(uname=uname,upwd=upwd)
        if users:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败')

def widget01(request):
    form = WidgetRegisterForm()
    return render(request,'02-widget01.html',locals())

def set_cookie(request):
    resp = HttpResponse('成功响应数据到客户端')
    expires = 60*60*24*365
    resp.set_cookie('USERID','66998877',expires)
    return resp

def get_cookie(request):
    # print(request.COOKIES['USERID'])
    if 'USERID' in request.COOKIES:
        print('USERID的值为:'+request.COOKIES['USERID'])
    return HttpResponse('获取cookies成功')

def set_session(request):
    request.session['USERID'] = '66998877'
    request.session['UNAME'] = 'CHENHAUQI'
    return HttpResponse('session数据保存成功')


def get_session(request):
    uid = request.session['USERID']
    uname = request.session['UNAME']
    return HttpResponse('UID:%s,UNAME:%s' % (uid,uname))



