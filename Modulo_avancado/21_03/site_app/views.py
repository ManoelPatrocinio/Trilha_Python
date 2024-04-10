from django.shortcuts import render
from site_app.models import produto
# Create your views here.
def home (request): 
    produtoData = produto.objects.order_by('id')
    print(produtoData)
    context = {'produto': produtoData}
    return render(request,'home.html',context)


def page_roupas (request):
    produtoData = produto.objects.order_by('id')
    context = {'produtos': produtoData}
    return render(request,'roupas.html',context)

def page_roupa_detalhe(request, produto_id):
    produto = produto.objects.get(id=produto_id)
    context = {'produto':produto}
    return render(request,'refeicao.html',context)