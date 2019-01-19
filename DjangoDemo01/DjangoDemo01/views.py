from django.http import HttpResponse

def show(request):
    return HttpResponse('这是DjangoDemo01')