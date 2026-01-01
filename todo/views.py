from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from todo import models
from todo.models import TODO
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404




from django.contrib import messages
from django.contrib.auth.models import User

def signUp(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email = request.POST.get('email')
        pwd = request.POST.get('password')

        # username already exists?
        if User.objects.filter(username=fnm).exists():
            messages.error(request, 'Username already exists!')
            return redirect('signup')

        # email already exists?
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('signup')

        User.objects.create_user(username=fnm, email=email, password=pwd)
        messages.success(request, 'Account created successfully!')
        return redirect('/logIn')

    return render(request, 'signUp.html')


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

@login_required
def TodoPage(request):
    if request.method=='POST':
        title=request.POST.get('titles').strip()
        if title:
            obj=models.TODO(title=title,user=request.user)
            obj.save()
        res=models.TODO.objects.filter(user=request.user).order_by('-created_at')
        return redirect('/TodoPage')
    res=models.TODO.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'todoPage.html',{'res':res})

@login_required
def edit_title(request,id):
        if request.method=='POST':
            title=request.POST.get('titles').strip()
            if title:
                obj=models.TODO.objects.get(id=id,user=request.user)
                obj.title=title
                obj.save()
            res=models.TODO.objects.filter(user=request.user).order_by('-created_at')
            return redirect('/TodoPage')
        obj=models.TODO.objects.get(id=id)
        return render(request, 'edit_title.html', {'obj': obj})

@login_required
def delete_todo(request, id):
    todo = get_object_or_404(TODO, id=id, user=request.user)
    todo.delete()
    return redirect('TodoPage')


def logout_view(request):
    logout(request)
    return redirect('logIn')


