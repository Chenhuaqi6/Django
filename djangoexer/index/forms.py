from django import forms

from .models import *


class RegisterForm(forms.Form):
    uname = forms.CharField(label='用户名称')
    upwd = forms.CharField(label='用户密码')
    uage = forms.IntegerField(label='用户年龄')
    uemail = forms.EmailField(label='电子邮箱')


class ModelRegisterForm(forms.ModelForm):
    class Meta:
        # 1.指定关联的model类 - model
        model = Users
        # 2.指定要生成控件的字段们 - fields
        fields = "__all__"
        # 3.指定每个属性对应的label - labels
        labels = {
            'uname':'用户名称',
            'upwd':'用户密码',
            'uage':'用户年龄',
            'uemail':'电子邮件'
        }

class ModelLoginFrom(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["uname",'upwd']
        labels = {
            'uname' : "用户名",
            'upwd':'密码',
        }

LEVEL_CHOICE = (
    ('1','好评'),
    ('2','中评'),
    ('3','差评'),
)
class WidgetRegisterForm(forms.Form):
    #用户名称 - type - text
    uname = forms.CharField(
        label='用户名称',
        widget = forms.TextInput(attrs={'placeholder':'请输入用户名','class':'form-control'}),
    )
    #用户密码 - type - password
    upwd = forms.CharField(
        label='用户密码',
        widget = forms.PasswordInput(attrs={'placeholder':'请输入密码','class':'form-control'}),
    )
    #评论级别 type - radio
    level = forms.ChoiceField(
        label='评论级别',
        choices=LEVEL_CHOICE,
        widget = forms.RadioSelect
    )
