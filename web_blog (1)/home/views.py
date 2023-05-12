from django.core.checks import messages
from django.http import request
from django.shortcuts import render , HttpResponse
from django.contrib.auth.models import User
from home.models import contact
from blog.models import post
from random import randint
# Create your views here.
def home(request):
    prod= post.objects.all()
    allprod={'allprod':prod}
    return render(request,'home\home.html',allprod) 
def code(request):
    return render(request,'home/h.html')
def about(request):
    return render(request,'home/about.html')
def cntact(request):
    if(request.method=='POST'): 
        x=randint(0,10000000)
        no= request.POST.get('name')
        eo= request.POST.get('email')
        po= request.POST.get('phone')
        d0= request.POST.get('desc')
        k= contact(x,eo,d0,po,no) 
        k.save()
        
    return render(request,'home/contact.html')
def comp(request):
    name= request.GET.get('code')
    return HttpResponse(name)
def search(request):
    allprod=post.objects.none()
    qry= request.GET.get('search')
    allprodtitle= post.objects.filter(title__icontains =qry)
    allprodcontent= post.objects.filter(blog_post__icontains =qry)
    allprod=allprodtitle.union(allprodcontent)
    p={'allprod':allprod}
    return render(request,'home/search.html',p)
def signup(request):
    if request.method =='post':
        name=request.POST.get('user_name')
        email=request.POST.get('email')
        p1=request.POST.get('p1')
        p2=request.POST.get('p2')
        myuser=User.objects.create(name,email,p1)
        myuser.save()
    return HttpResponse("hello")