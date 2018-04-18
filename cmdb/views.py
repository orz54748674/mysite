# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from django.shortcuts import render
from cmdb import models
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if models.UserInfo.objects.filter(user=username).count() > 0:
            return HttpResponse("用户名已存在")
        #添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
        return HttpResponse("注册成功")
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        q = models.UserInfo.objects.filter(user=username)
        for obj in q:
            if obj.pwd == password:
                if username == "lwl":
                    # 从数据库中读取所有数据
                    user_list = models.UserInfo.objects.all()
                    return render(request, "login_admin.html", {"data": user_list})
                return render(request, "login_default.html")
        return HttpResponse("用户名或密码错误")
    return render(request, "login.html")