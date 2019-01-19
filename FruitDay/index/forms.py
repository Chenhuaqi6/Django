from django import forms
from .models import *

class LoginModelForm(forms.ModelForm):
    class Meta:
        #属性1:uphone
        #属性2:upwd
        #1.指定关联的实体类
        model = Users
        #2.指定取出哪些字段生成控件
        fields = ['uphone','upwd',]
        #3.指定每个控件的label
        labels = {
            'uphone':'手机号',
            'upwd':'密码',
        }
        #4.指定每个控件的小部件
        widgets = {

            'uphone':forms.TextInput(attrs={'placeholder':'请输入手机号','class':'uinput'}),
            'upwd':forms.PasswordInput(attrs={'placeholder':'请输入密码6-20为位','class':'uinput'})
        }