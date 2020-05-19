from django.contrib import admin

# Register your models here.
from .models import Pizza,Topping,Subs,Pasta,Salad,Dinnerplatter,Orderhistory,Cart
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinnerplatter)
admin.site.register(Orderhistory)
admin.site.register(Cart)

