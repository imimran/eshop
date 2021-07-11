from django.http import request
from django.shortcuts import redirect, render
from .form import UserRegistationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'demo.html')

    
def register(request):
    context={}
    if request.POST:
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form'] = form

    else:
         form = UserRegistationForm()
         context['register_form']= form
    return render(request, 'register.html', context)


def login_view(request):
    context={}
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
                
    form = UserLoginForm()
    context['login_form']=form
    return render(request,'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

def forgot_password(request):
    return render(request, 'forgot_password.html')
