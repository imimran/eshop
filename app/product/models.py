from django.db import models
import uuid
import os
from accounts.models import MerchantUser, CustomerUser, StaffUser, AdminUser
# Create your models here.


def category_image_path(instance, filename):
    """ Genereate image path for recipe"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('category/', filename)


class Categories(models.Model):
    title=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    thumbnail=models.FileField()
    description=models.TextField()
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.IntegerField(default=1)

    def __str__(self):
        return str(self.title)



class Products(models.Model):
    slug=models.CharField(max_length=255)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    product_max_price=models.CharField(max_length=255)
    product_discount_price=models.CharField(max_length=255)
    product_description=models.TextField()
    product_long_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by_merchant=models.ForeignKey(MerchantUser,on_delete=models.CASCADE)
    in_stock_total=models.IntegerField(default=1)
    is_active=models.IntegerField(default=1)

class ProductMedia(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    media_type_choice=((1,"Image"),(2,"Video"))
    media_type=models.CharField(max_length=255)
    media_content=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.IntegerField(default=1)  

class ProductTransaction(models.Model):
    transaction_type_choices=((1,"BUY"),(2,"SELL"))
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    transaction_product_count=models.IntegerField(default=1)
    transaction_type=models.CharField(choices=transaction_type_choices,max_length=255)
    transaction_description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ProductDetails(models.CharField):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    title_details=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.IntegerField(default=1)

class ProductAbout(models.CharField):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.IntegerField(default=1)

class ProductTags(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProductQuestions(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProductReviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    review_image=models.FileField()
    rating=models.CharField(default="5", max_length=50)
    review=models.TextField(default="")
    updated_at = models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProductReviewVoting(models.Model):
    product_review_id=models.ForeignKey(ProductReviews,on_delete=models.CASCADE)
    user_id_voting=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProductVarient(models.Model):
    title=models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

class ProductVarientItems(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

