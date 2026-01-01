from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from todo import models
from todo.models import TODO


def signUp(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        my_user=User.objects.create_user(fnm,email,pwd)
        my_user.save()
        return redirect('/logIn')
    return render(request,'signUp.html')


def logIn(request):
    if request.method=='POST':
        fnm=request.POST.get('Username')
        pwd=request.POST.get('password')
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/TodoPage')
        else:
            return redirect('/logIn')      
    return render(request,'logIn.html')

def TodoPage(request):
    if request.method=='POST':
        titlle=request.POST.get('titles')
        obj=models.TODO(title=titlle,user=request.user)
        obj.save()
        res=models.TODO.objects.filter(user=request.user).order_by('-created_at')
        return redirect('/TodoPage',{'res':res})
    res=models.TODO.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'todoPage.html',{'res':res})