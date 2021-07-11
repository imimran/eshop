from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def adminLogin(request):
    return render(request, 'admin_section/login.html')

@login_required(login_url='/admin/')
def admin_dashboard(request):
    return render(request, 'admin_section/home.html')


def admin_login_process(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request=request, email=email, password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_dashboard"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("admin_login"))


def admin_logout_process(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return HttpResponseRedirect(reverse("admin_login"))
