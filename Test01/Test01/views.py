from django.http import HttpResponse

#Django中的视图处理函数中必须有一个参数,名称必须叫request

def show(request):
    return HttpResponse('我的第一个Django程序')

def show_01(request):
    return HttpResponse("这是show_01的访问结果")

#匹配地址:http://localhost:8000/show_02/四位整数
#参数year:表示的就是地址中的四位整数
def show_02(request,year):
    return HttpResponse("传递过来的参数为:"+year)

def show_03(request,year,mounth,day):
    return HttpResponse("生日为:%s年%s月%s日" % (year,mounth,day))