from django.db import models
from accounts.models import *
TYPES = (
    ('0', 'T-shirts'),
    ('1', 'Shirts'),
    ('2', 'Blazers'),
('3', 'Kurtas'),
    ('4', 'Jeans'),
    ('5', 'Trousers'),
    ('6', 'Shorts'),
    ('7', 'Hoodies'),
    ('8', 'Jackets'),
    ('9', 'Sweaters'),
    ('10', 'Men shoes'),
    ('11', 'Kurtas'),
('12', 'Salwar suits'),
    ('13', 'Sarees'),
    ('14', 'Tops'), 
   ('15', 'Jeans'),
    ('16', 'Coats and Jackets'),
    ('17', 'Women Hoddies'),
('18','Cardigans'),
('23','Women Shoes'),
('19','Kids Jackets'),
    ('20', 'Girls dresses'),
    ('21', 'Boys dresses'),
    ('22', 'Kids sweatshirts'),
 )
class Product(models.Model):
    product_no = models.CharField(max_length = 30,null= True)
    category = models.CharField(max_length = 30,choices = TYPES, null= True)
    sub_category = models.CharField(max_length = 30,null= True,blank =True)
    stock = models.CharField(max_length = 30,default=10)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    company = models.CharField(verbose_name='Com', max_length=500, blank=True, null=False)
    price = models.CharField(verbose_name='price', max_length=500)
    description= models.TextField()
    #shop, stock available, (warranty, garranty,insurance=null==true,blank ==true,),description of all,
    shop=models.CharField(max_length=30,null=True)
    stock_available=models.CharField(max_length=30)
    warranty=models.CharField(max_length=30,null=True,blank=True)
    warranty_desc=models.TextField()
    insurance=models.CharField(max_length=30,null=True,blank=True)
    insurance_desc=models.TextField()
    garranty=models.CharField(max_length=30,null=True,blank=True)
    garranty_desc=models.TextField()
    def __str__(self):
        return (self.user + self.category + self.product_no)
