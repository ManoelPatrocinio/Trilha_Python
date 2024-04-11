from django.shortcuts import render
from site_app.models import produto
# Create your views here.

def home (request): 
    produtoData = produto.objects.order_by('id')
    context = {'produtos': produtoData} 
    return render(request,'home.html',context)

def page_roupas (request):
    produtoData = produto.objects.order_by('id')
    context = {'produtos': produtoData} 
    return render(request,'roupas.html',context)

def page_roupa_detalhe(request, produto_id):
    produtoData = produto.objects.get(id=produto_id)
    context = {'produto':produtoData}
    return render(request,'roupa_detalhe.html',context)

def page_login (request): 
    return render(request,'login.html')

def page_registro (request): 
    return render(request,'registro.html')
