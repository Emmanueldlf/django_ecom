from django.contrib import admin
from .models import Product
from .models import Order

# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Net Shop"
admin.site.index_title = "Manage Net Shop"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category = "default")


    change_category_to_default.short_description = 'Default Category'
    list_display = ('name','price','discounted_price','category','description','image')
    search_fields = ('name',)
    actions = ('change_category_to_default',)
    fields = ("name", "price",)
    list_editable = ("price","category",)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
