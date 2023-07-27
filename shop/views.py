from django.shortcuts import render
from .models import Product
from .models import Order
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Product.objects.all()

    #Search feature
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(name__icontains=item_name)

    #Pagination feature
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)


    return render(request, 'shop/index.html', {'product_objects':product_objects})

def detail(request, id):
    product_objects = Product.objects.all()
    product_object = product_objects.get(id=id)

    return render(request, 'shop/detail.html', {'product_object':product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get("email","")
        address = request.POST.get("address","")
        address2 = request.POST.get("address2","")
        state = request.POST.get("state","")
        city = request.POST.get("city","")
        zip = request.POST.get("zip","")
        total=request.POST.get("total","")

        order = Order(items=items,name=name,email=email,address=address,address2=address2,state=state,city=city,zip=zip,total=total)
        order.save()

    return render(request,'shop/checkout.html')
