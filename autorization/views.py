from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from shavarma import views
from shavarma.views import homepage
# Create your views here.


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'autorization/signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect(homepage)
            except IntegrityError:
                return render(request, 'autorization/signup.html', {'error':'Данный пользователь уже зарегестрирован в системе'})
            else:
                return render(request, 'autorization/signup.html', {'error':'Пароли не совпадают'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'autorization/login.html')
    else:
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'autorization/login.html',{'error':'Проверьте правильность введенных данных'})
        else:
            login(request,user)
            return redirect(homepage)

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(homepage)
