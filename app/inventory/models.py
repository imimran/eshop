from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title


class Purchase(models.Model):
    supplier_name= models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  

    def __str__(self) -> str:
        return self.product.title 


    def save(self, *args, **kwargs)-> int:
        super().save(*args, **kwargs)
        self.product.quantity = self.product.quantity + self.quantity 
        self.product.save()

    
