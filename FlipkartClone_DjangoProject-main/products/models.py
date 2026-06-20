from django.db import models

# Create your models here.

class Product(models.Model):
    ID=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=50,default='n/a')
    name=models.CharField(max_length=50)
    CATEGORY_CHOICES = [
    ('Electronics', 'Electronics'),
    ('Clothing', 'Clothing'),
    ('Shoes', 'Shoes'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description=models.CharField(max_length=150)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    image=models.ImageField(upload_to="Media/Images")
    pdfs=models.FileField(upload_to="Media/pdfs",null=True,blank=True)


# from django.db import models

# class Product(models.Model):

#     name = models.CharField(max_length=100)
#     CATEGORY_CHOICES = [
#         ('Electronics', 'Electronics'),
#         ('Clothing', 'Clothing'),
#         ('Shoes', 'Shoes'),
#     ]
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to="images/", null=True, blank=True)
#     pdfs = models.FileField(upload_to="pdfs/", null=True, blank=True)
#     def __str__(self):
#         return self.name