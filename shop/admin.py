from django.contrib import admin
from .models import Product
from .models import Order

# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Net Shop"
admin.site.index_title = "Manage Net Shop"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','discounted_price','category','description','image')

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
