# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from people.forms import AddForm
import json
from people.models import Person , Author
# Create your views here.

def index(request):
  return render(request,'people/index.html')

def add(request):
  a = request.GET['a']
  b = request.GET['b']
  a = int (a)
  b = int (b)
  
  if request.is_ajax():
    return HttpResponse(str(a+b))
  else:
    return HttpResponse(str(a+b))
#测试
def test(request):
  return HttpResponse(u"人生苦短，学习python")

# 引入我们创建的表单类
# from .forms import AddForm

def index2(request):
  if request.method=='POST':
     
      form = AddForm(request.POST)#request包含提交的数据
      if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        return HttpResponse(str(int(a)+int(b)))
  else:#当正常访问时
    form=AddForm()
  return render(request,'people/index2.html',{'form':form})
      
def ajax_list(request):
  a = range(100)
  return HttpResponse(json.dumps(a),content_type="application/json")

def ajax_dict(request):
  name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
  return HttpResponse(json.dumps(name_dict), content_type='application/json')

def Ajax(request):
  return render(request,'people/Ajax.html')


def queryapi(request):
    # 方法 1
  Author.objects.create(name="WeizhongTu", email="tuweizhong@163.com")

  # 方法 2
  twz = Author(name="WeizhongTu2", email="tuweizhong@1632.com")
  twz.save()

  # 方法 3
  twz = Author()
  twz.name="WeizhongTu3"
  twz.email="tuweizhong@1633.com"
  twz.save()

  # 方法 4，首先尝试获取，不存在就创建，可以防止重复
  Author.objects.get_or_create(name="WeizhongTu", email="tuweizhong@163.com")
  # 返回值(object, True/False)
  #查询
#   a=Author.objects.all()
  b=Author.objects.get(name='WeizhongTu')
  return HttpResponse(b.email) 
#   for b,c in a:
#     
  c=b.objects.get(email='tuweizhong@163.com')
  if ture :
      return HttpResponse(1)
  else:
      return HttpResponse(0)
  return HttpResponse(a)
      
  