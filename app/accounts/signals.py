from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import AdminUser, CustomerUser, MerchantUser, StaffUser, User

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 1:
            AdminUser.objects.create(User = instance)

        if instance.role == 2:
            StaffUser.objects.create(User = instance)

        if instance.role == 3:
            MerchantUser.objects.create(User = instance)

        if instance.role == 4:
            CustomerUser.objects.create(User = instance)

@receiver(post_save, sender= User)
def save_user_profile(sender, instance, **kwargs):
    if instance.role==1:
        instance.adminuser.save()
    if instance.role==2:
        instance.staffuser.save()
    if instance.role==3:
        instance.merchantuser.save()
    if instance.role==4:
        instance.customeruser.save()