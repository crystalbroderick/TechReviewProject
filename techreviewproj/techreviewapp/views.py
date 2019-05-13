from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review


# Create your views here.
def index(request):
    return render(request, 'techreviewapp/index.html')

def getTypes(request):
    types_list=TechType.object.all() # or you can do .filter 
    context={'types_list': types_list }
    return render(request, 'techreviewapp/types.html', context=context) 

def getProducts(request):
    products_list=Product.objects.all()
    return render(request, 'techreviewapp/products.html', {'products_list': products_list})

def productDetail(request, id):
    prod=get_object_or_404(product, pk=id)
    reviewcount=Review.objects.filter(product=id).count()
    reviews=Review.objects.filter(product=id)
    context={
        'prod' : prod,
        'reviewcount' : reviewcount,
        'reviews': reviews, 
    }
    return render(request, 'techreviewapp/productdetail.html', context=context)