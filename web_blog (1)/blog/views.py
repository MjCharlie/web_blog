from django.shortcuts import render , HttpResponse
from blog.models import post
# Create your views here.
def home(request):
    prod=post.objects.all()
    print(prod)
    allprod={'allprod':prod}
    return render(request,'blog/home.html',allprod)
def ping(request,slg):
    prod=post.objects.filter(slug=slg).first()
    print(prod)
    allprod={'allprod':prod}
    return render(request,'blog/blog.html',allprod)