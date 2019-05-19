from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review
from .forms import ProductForm, ReviewForm

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

def newProduct(request):
    form=ProductForm
    if request.method=='POST':
        form=ProductForm(request.POST) # upper case POST is a constant
        if form.is_valid():
            post=form.save(commit=True) # lower case post is a variable
            post.save()
            form=ProductForm() # not required, but this clears data when done w/ form
    else:
        form=ProductForm()
    return render(request, 'techreviewapp/newproduct.html', {'form': form})

def newReview(request):  
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST) # upper case POST is a constant
        if form.is_valid():
            post=form.save(commit=True) # lower case post is a variable
            post.save()
            form=ReviewForm() # not required, but this clears data when done w/ form
    else:
        form=ReviewForm()
    return render(request, 'techreviewapp/newreview.html', {'form': form})