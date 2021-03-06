from django.http import HttpResponse
from django.shortcuts import render
from  .forms import *
# Create your views here.
def test_views(request):
    return  HttpResponse("<a href='/01-request/'>测试链接</a>")

def request_views(request):
    # print(dir(request))
    print('request.scheme:%s' % request.scheme)
    print('request.path:%s' % request.path)
    print('request.method:%s' % request.method)
    print('request.GET:',request.GET)
    print('request.POST:',request.POST)
    print('request.COOKIES:',request.COOKIES)
    print('request.META:',request.META)
    #判断有没有请求的源地址
    if 'HTTP_REFERER' in request.META:
        print('请求源地址:',request.META['HTTP_REFERER'])
    else:
        print('没有请求源地址')
    return  HttpResponse('请求对象获取成功')

def post_views(request):
    #判断请求方式
    # 如果是get去往02-post.html
    #如果是post则接收请求提交的数据
    if request.method == 'GET':
        return render(request,'02-post.html')
    else:
        #接收前端传递过来的uname和upwd
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')

        return HttpResponse('用户名称:%s,用户密码:%s' % (uname,upwd))

def form_views(request):
    #创建RemarkForm的UI小,并发送到03-form.html上
    if request.method == "GET":
        form = RemarkForm()
        return render(request,'03-from.html',locals())
    else:
        #通过forms模块来获取提交的数据
        #1.提交的数据交给RemarkForm()
        form = RemarkForm(request.POST)
        #2.通过验证
        if form.is_valid():
        #3.取值
            cd = form.cleaned_data
            print(cd)
            return  HttpResponse('取值成功')
        return HttpResponse('取值失败')
