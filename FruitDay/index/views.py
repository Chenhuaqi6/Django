from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,"index.html")
def cart(request):
    return render(request,'cart.html')
def register(request):
    #判断请求方式
    #get:看 register.html
    #post : 处理请求提交数据
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        #post请求处理
        #获取uphone的内容,没判断其是否存在
        uphone = request.POST['uphone']
        users = Users.objects.filter(uphone=uphone)
        if users:
            #uphone已经存在
            return render(request,'register.html',{'errMsg':'手机号码已存在'})
        else:
            #将前端数据取出来赋值给users
            users = Users()
            users.uphone = uphone
            users.upwd = request.POST['upwd']
            users.uemail = request.POST['uemail']
            users.uname = request.POST['uname']
            #将users保存进数据库
            #成功取首页,失败的话则给出提示
            try:
                users.save()
                return redirect('/')
            except Exception as ex:
                print(ex)
                return render(request,'register.html',{'errMsg':'请联系管理员'})





def modellogin(request):
    if request.method == 'GET':
        #获取请求源地址,没有的话,则获取'/' 存session中
        url = request.META.get('HTTP_REFERER','/')
        request.session['url'] = url
        #先判断session中是否有信息
        if 'id' in request.session and 'uphone' in request.session:
            #如果有则从哪来回哪去
            print(url)
            return redirect(url)
        else:
            #否则继续判断cookie中是否有登录信息
            if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
                id = request.COOKIES['id']
                uphone = request.COOKIES['uphone']
                users = Users.objects.filter(id=id,uphone=uphone)
                if Users:
                    #如果有则取出来判断,如果正确存session,并从哪来回哪去
                    request.session['id'] = id
                    request.session['uphone'] = uphone
                    return redirect(url)
                else:
                    #如果不正确,先删除cookies中原有的值,再回到首页
                    #构建响应对象并删除cookies的值再返回
                    form = LoginModelForm()
                    resp = render(request, 'login.html', {'form':form})
                    resp.delete_cookie('id')
                    resp.delete_cookie('uphone')
                    return resp



            else:
                #如果没有则取登录界面
                #创建LoginForm()并交给html
                form = LoginModelForm()
                return render(request, 'login.html', locals())
    else:
        #获取手机号码和密码,验证登录
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        user = Users.objects.filter(uphone=uphone,upwd=upwd)
        print(user[0].id)
        #成功:向下执行
        if user:
            #将id和uphone存进session
            request.session['id'] = user[0].id
            request.session['uphone'] = uphone
            #从session中获取源地址,并构建响应对象
            url = request.session['url']
            resp = redirect(url)
            #判断是否要记住密码(保存进cookie)
            if 'savepwd' in request.POST:
                expire = 60*60*24*365
                resp.set_cookie('id',user[0].id,expire)
                resp.set_cookie('uphone',uphone,expire)
            #从哪来回哪去
            return resp
        #失败:回登录页
        else:
            form = LoginModelForm()
            return render(request, 'login.html', locals())