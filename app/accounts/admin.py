from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'status', 'created_at','updated_at')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'phone', 'address', 'role')


admin.site.unregister(Group)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.User )
# admin.site.unregister(Group)
