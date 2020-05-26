from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def insert(request):
    return HttpResponse("he")
def load(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    if(username=="123" and password=="456"):
        return HttpResponse("登陆成功")
    else:
        return HttpResponse("登陆失败")
