from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . models import *
from django.core.paginator import Paginator

# Create your views here.

def index(request,c_slug=None):

    if c_slug!=None:
        c_page=get_object_or_404(cate,slug=c_slug)
        pro=product.objects.filter(category=c_page,available=True)
    else:
        pro=product.objects.all().filter(available=True)


    paginator = Paginator(pro, 1)

    page = request.GET.get('page')
    paginated = paginator.get_page(page)


    obj=cate.objects.all()           #var = model_name.data.all()
    return render(request, 'index.html',{'c': obj,'p': pro,"paginated":paginated})

def details(request,c_slug,product_slug):
    prodt = get_object_or_404(product, category__slug=c_slug, slug=product_slug)
    return render(request,'product-single.html',{'pro':prodt})

def search(request):
    if 'q' in request.GET:
        query=request.GET.get('q')

        prod=product.objects.all().filter(Q(name__icontains=query)|Q(desc__icontains=query),available=True)
    return render(request,'search.html',{'pr':prod})                               #CONTEXT

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request,'Contact.html')









