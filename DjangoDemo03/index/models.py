from django.db import models

#创建自定义的objects的类型 - EntryManager
class AuthorManager(models.Manager):
    #自定义方法 - 查询大于指定年龄的Author的数量
    def age_count(self,age):
        return self.filter(age__gte=age).count()
    def name_contain(self,name):
        return self.filter(name__contains=name).all()

class BookManager(models.Manager):
    def year_time(self,year):
        return self.filter(publicate_date__year=year).all()


# Create your models here.

#创建一个实体类-Publisher
#表示出版社信息,属性如下:
#1.name:出版社名称(varchar)
#2.address:出版社所在地址(varchar)
#3.city:出版社所在城市(varchar)
#4.country:出版社所在国家(varchar)
#5.website:出版社网址(varchar)
#6.Django中自带自增的id
# class Publisher(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=200)
#     city = models.CharField(max_length=20)
#     country = models.CharField(max_length=20)
#     website = models.URLField() #长度默认200

class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    address = models.CharField(max_length=200,verbose_name='出版地址')
    city = models.CharField(max_length=20,verbose_name='所在城市')
    country = models.CharField(max_length=20,verbose_name='所在国家')
    website = models.URLField(verbose_name='官方网址')
    #通过 __str__ 修改展现形式
    def __str__(self):
        return self.name
    class Meta:
        #1.指定表名
        db_table = 'publisher'
        #2.指定后台展现名称(单数)
        verbose_name = '出版社'
        #3.指定后台展现名称(复数)
        verbose_name_plural = verbose_name
        #4.指定排序方式


class Author(models.Model):
    #通过AuthorManager覆盖原有的objects
    objects = AuthorManager()
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱')
    #增加isActive表示是否处于启用状态 - models.BooleanField
    isActive = models.BooleanField(default=True,verbose_name='活动用户')

    #通过 __str__ 修改展现形式
    def __str__(self):
        return self.name

    class Meta:
        #1.指定表名
        db_table = 'author'
        #2.指定后台展现名称(单数)
        verbose_name = '作者'
        #3.指定后台展现名称(复数)
        verbose_name_plural = verbose_name
        #4.指定排序方式
        ordering = ['age','-id']

class   Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=30,verbose_name='书名')
    publicate_date = models.DateField(verbose_name='出版日期')
    #增加对Publisher(一)的引用关系
    publisher = models.ForeignKey(Publisher,null=True,verbose_name='出版社')
    #增加对Author(多)的引用关系
    author_set = models.ManyToManyField(Author)
    #通过 __str__ 修改展现形式
    def __str__(self):
        return self.title

    class Meta:
        #1.指定表名
        db_table = 'book'
        #2.指定后台展现名称(单数)
        verbose_name = '书籍'
        #3.指定后台展现名称(复数)
        verbose_name_plural = verbose_name
        #4.指定排序方式
        ordering = ['-publicate_date']



#Wife - 夫人
#name,age
class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    #增加属性-author 表示与Author表的一对一关系
    author = models.OneToOneField(Author,null=True,verbose_name='丈夫')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'wife'
        verbose_name = '夫人'
        verbose_name_plural = verbose_name


































