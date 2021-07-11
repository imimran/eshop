"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts import views
from accounts import admin_views

admin.site.site_header = "E-Shop Management"
admin.site.site_title = "E-Shop Management"
admin.site.index_title = "Welcome to E-Shop Management"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin_views.adminLogin, name='admin_login'),
    path('user/', include('accounts.urls')),
    path('admin-login', admin_views.admin_login_process, name='admin_login_process'),
    path('admin-logout', admin_views.admin_logout_process, name='admin_logout_process'),
    path('admin-dashboard', admin_views.admin_dashboard, name='admin_dashboard'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
