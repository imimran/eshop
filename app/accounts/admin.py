from django.contrib import admin
from django.contrib.auth.models import Group
from .models import AdminUser, CustomerUser, MerchantUser, StaffUser, User

# Register your models here.

# class RoleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'code', 'status', 'created_at','updated_at')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'phone', 'address', 'role')



# admin.site.register(models.Role, RoleAdmin)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin )
admin.site.register(AdminUser )
admin.site.register(CustomerUser )
admin.site.register(MerchantUser )
admin.site.register(StaffUser )


