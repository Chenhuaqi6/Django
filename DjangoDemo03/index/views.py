from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Sum, Avg, Count


# Create your views here.
def add_author(request):
    # #使用Entry.objects.create() 实现增加数据
    # author = Author.objects.create(name='莫言',age=65,email='moyan@163.com')
    # print(author)

    #创建Entry的对象,并调用其save()
    # author = Author(name='鲁迅',age=95)
    # author.email = 'zhoushuren@163.com'
    # author.save()


    #使用字典创建对象,并调用其save方法
    dic = {
        'name':'巴金',
        'age':100,
        'email':'eightjin@163.com',
        'isActive': False,
    }
    author = Author(**dic)
    author.save()
    print('ID:'+str(author.id))
    print('Name:'+author.name)
    print('Age:'+str(author.age))
    print('Email:'+author.email)
    print('isActive:'+str(author.isActive))
    return HttpResponse("<script>alert('增加数据成功');</script>")

def add_book(request):
    #使用Entry.objects.create()
    # book = Book.objects.create(title='<<狂人日记>>',publicate_date = '1921-11-11')

    # #使用Entry对象,调用save()
    # book = Book(title='丰乳肥臀',publicate_date='1988-10-15')
    # book.save()

    #使用字典创建对象,并调用save()
    dic={
        'title':'<<红高粱>>',
        'publicate_date':'1995-12-15'
    }
    book = Book(**dic)
    book.save()
    return HttpResponse("<script>alert('增加数据成功');</script>")

def add_publisher(request):
    #使用Entry.objects.create()
    pub = Publisher.objects.create(name='中国人民出版社',address='杭州余杭区旭辉府',city = '杭州',country='中国',website='www.chenhuaqi.com')
    return HttpResponse("<script>alert('增加数据成功');</script>")

def query(request):
    ##################
    ###1.all()
    #################

    # authors = Author.objects.all()
    # print(authors.query)
    #循环遍历authors的每条数据
    # for au in authors:
    #     print("ID:%d,Name:%s,Age:%s" % (au.id,au.name,au.age))
    ##################
    ###2.values()
    #################
    #authors = Author.objects.values()
    authors = Author.objects.values('id','email')
    print(authors)
    # for au in authors:
    #     print('ID:%d,Name:%s'% (au['id'],au['name']))
    return HttpResponse("<script>alert('查询数据成功')</script>")

def queryall(request):
    # authors = Author.objects.all()
    #1.查询出isACTIV为True的信息
    authors = Author.objects.filter(isActive=True)
    return render(request,'03-queryall.html',locals())

def filter_query(request):

    #2.查询id为1并且name为,莫言的Author的信息
    authors = Author.objects.filter(id=1,name='莫言')
    print(authors.query)
    print(authors)
    return HttpResponse('query ok')

def filter_aa(request):
    author1 = Author.objects.filter(age__gt=95)
    for au1 in author1:
        print(au1.name,au1.age)
    #姓鲁的
    author2 = Author.objects.filter(name__startswith='鲁')
    for au2 in author2:
        print(au2.name,au2.age)
    #包含sh
    author3 = Author.objects.filter(email__contains='sh')
    for au3 in author3:
        print(au3.name,au3.age,au3.email)
    #查询年级大于鲁迅的年纪的人的信息
    author4 = Author.objects.filter(age__gt=(Author.objects.filter(name='鲁迅').values('age')))
    for au4 in author4:
        print(au4.name,au4.age)
    #不等条件查询-exclude
    #1.查询id不等于1 的所有的Author的信息
    author5 = Author.objects.exclude(id=1)
    for au5 in author5:
        print(au5.name)

    #2.查询年龄不大于100的Author的信息

    author6 = Author.objects.exclude(age__gt=100)
    print('**************')
    for au6 in author6:
        print(au6.name)

    #排序
    author7 = Author.objects.order_by('-age')
    print(author7.query)
    print(author7.values('name','age'))
    return HttpResponse('查询成功')

# def update(request):
#     id = request.
#     author = Author.objects.get(id=id)
#     return render(request,'05-update.html',locals())

def update(request,id):
    #1.根据id查询出对应的Author的信息
    author=Author.objects.get(id=id)
    print(author)
    #2.将Author的信息渲染到05-update.html模板
    return render(request,'05-update.html',locals())

def aggregate(request):
    #1.查询author中年纪总和
    RESULT = Author.objects.aggregate(sumAge = Sum('age'))
    print(RESULT)

    #2.查询平均年龄
    ping = Author.objects.aggregate(avgAge = Avg('age'))
    print(ping)

    #3.年纪大于=90的人的数量
    cont = Author.objects.filter(age__gte=90).aggregate(countPeople = Count('age'))
    print(cont)
    return HttpResponse('Query ok')

def annotate(request):
    result = Author.objects.values('isActive').annotate(count = Count('*')).values('count')
    print(result)
    return HttpResponse('query ok')

def exercise(request):
    result = Book.objects.aggregate(count = Count('title'))
    print(result)
    result1 = Book.objects.values('publicate_date').annotate(count = Count('*')).values('count')
    print(result1)
    result2 = Book.objects.filter(publicate_date__year__gte='1954').aggregate(count = Count('*'))
    print(result2)
    result3 = Publisher.objects.filter(city__exact='杭州').aggregate(count = Count('*'))
    print(result3)
    return HttpResponse('ok')

def update08(request):
    # #1.获取 '巴金'
    # au = Author.objects.get(name="巴金")
    # #2.修改其email的值
    # au.email = 'ailing@163.com'
    # #保存回数据库
    # au.save()

    #修改所有人的isActive的值为true
    Author.objects.all().update(isActive = True)
    return HttpResponse('update sucess')

def delete(request,id):
    #1.根据id查询出对应的author信息
    au = Author.objects.get(id=id)
    #2.将其的isActive的值修改为False
    au.isActive = False
    #3.再保存回数据库
    au.save()
    #4.响应:重定向回/03-queryall
    return redirect('/03-queryall')

def oto_views(request):
    #创建wife对象 并指定author信息再保存会数据库
    #方式1:通过author_id关联
    # wife = Wife()
    # wife.name = '莫夫人'
    # wife.age = 50
    # wife.author_id = 1
    # wife.save()

    #方式2:通过author关联
    # author = Author.objects.get(name='巴金')
    # wife = Wife()
    # wife.name = '巴夫人'
    # wife.age = 96
    # wife.author = author
    # wife.save()

    #查询
    #通过Author查询Wife
    # author = Author.objects.get(name='巴金')
    # wife = author.wife
    # print('作者姓名:%s,年龄:%d' % (author.name,author.age))
    # print('夫人姓名:%s,年龄:%d' % (wife.name,wife.age))

    #通过Wife查询Author
    wife = Wife.objects.get(id=1)
    author = wife.author
    print('作者姓名:%s,年龄:%d' % (author.name,author.age))
    print('夫人姓名:%s,年龄:%d' % (wife.name,wife.age))

    return HttpResponse('查询成功')

def onemany(request):
    # book = Book(title='<<大炮>>')
    # book.publicate_date = '1997-3-17'
    # book.publisher_id = 2
    # book.save()

    # book = Book(title='<<丰乳肥臀>>')
    # publicate_date = '1997-3-17'
    # pub = Publisher.objects.get(name='莫言')
    # book.publisher = pub
    # book.save()
    # return HttpResponse('增加数据成功')


    #正向查询 - 通过Book查询对应的Publisher
    #查询id为3的书籍信息
    book = Book.objects.get(id=3)
    # #查询对应的出版社
    publisher = book.publisher

    #反向查询 - 通过Publisher查询对应的所有的Book
    #查询中国人民出版社的信息
    pub = Publisher.objects.get(name='中国人民出版社')
    #查询对应的所有的数据 - book_set
    books = pub.book_set.all()

    return render(request,'11-otm.html',locals())

def mtm_views(request):
    # # #增加数据: 为Book绑定Author
    # # #查询Book - '射雕英雄传'
    # book = Book.objects.get(title='<<射雕英雄传>>')
    # # #查询Author - 金庸
    # author = Author.objects.get(name = '金庸')
    # # #关联Book和Author(如果插入多条关联数据,使用列表)
    # # book.author_set.add(author)
    #
    # #通过Book的remove()删除author的关联信息
    # book.author_set.remove(author)
   # return HttpResponse('增加数据ok')
    #正向查询 - 通过book查询Author
    #查询Book - 丰乳肥臀
    book = Book.objects.get(title='<<丰乳肥臀>>')
    #获取对应的所有的Author
    authors = book.author_set.all()

    #反向查询 - 通过Author 查找book
    #查询Author - 金庸
    au = Author.objects.get(name='金庸')
    #获取对应所出版社的书籍
    books = au.book_set.all()
    return render(request,'12-mtm.html',locals())

def objects_views(request):
    count = Author.objects.age_count(90)
    myname = Author.objects.name_contain('金')
    for au in myname:
        print(au.name,au.age)
    myyear = Book.objects.year_time('2018')
    print(myyear.values())
    return HttpResponse('年龄大于等于90岁的人共有%d人' % count)