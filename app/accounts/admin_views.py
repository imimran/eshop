from django.http import request
from django.shortcuts import redirect, render

def admin_home(request):
    return render(request, 'admin_section/home.html')