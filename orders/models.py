
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
	name=models.CharField(max_length=64 )
	smallPrice=models.DecimalField(max_digits=4,decimal_places=2)
	largePrice=models.DecimalField(max_digits=4,decimal_places=2)
	def __str__(self):
		return f"{self.name} ||   Small: $ {self.smallPrice}   Large: $ {self.largePrice}"

class Topping(models.Model):
	toppings=models.CharField(max_length=64)
	def __str__(self):
		return f"{self.toppings}"

class Subs(models.Model):
	nameSub=models.CharField(max_length=64)
	smallSub=models.DecimalField(max_digits=4,decimal_places=2,null=True, blank=True)
	largeSub=models.DecimalField(max_digits=4,decimal_places=2,null=True, blank=True)
	def __str__(self):
		return f"{self.nameSub} ||   Small: $ {self.smallSub}   Large: $ {self.largeSub}"

class Pasta(models.Model):
	pastaName=models.CharField(max_length=64)
	pricePasta=models.FloatField(null=True, blank=True,)
	def __str__(self):
		return f"{self.pastaName}   $ {self.pricePasta}"

class Salad(models.Model):
	saladName=models.CharField(max_length=64)
	priceSalad=models.FloatField(null=True, blank=True)
	def __str__(self):
		return f"{self.saladName}   $ {self.priceSalad}"

class Dinnerplatter(models.Model):
	nameDinn=models.CharField(max_length=64)
	smallDinn=models.DecimalField(max_digits=4,decimal_places=2,null=True, blank=True)
	largeDinn=models.DecimalField(max_digits=4,decimal_places=2,null=True, blank=True)
	def __str__(self):
		return f"{self.nameDinn} ||   Small: $ {self.smallDinn}   Large: $ {self.largeDinn}"

 #Order
class Orderhistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    

# Shopping Cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number=models.IntegerField(default=1)
    status=models.CharField(max_length=64,null=True, blank=True,default='initiated')
    cart_item = models.CharField(max_length=64)
    size=models.CharField(max_length=64, null=True, blank=True)
    extras = models.CharField(max_length=512, null=True, blank=True)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)
    delivery=models.CharField(max_length=512, default='notdelivered')
    
    
    class Meta:
        permissions=[
			('special_status', 'Can read all books')
		]
    
    
    # String representation of self
    def __str__(self):
        return f"    Item: {self.cart_item}  | Size:{self.size} |  Extras: {self.extras}  |  Price: {self.item_price}"

