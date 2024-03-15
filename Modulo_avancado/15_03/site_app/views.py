from django.shortcuts import render
from site_app.models import produto
# Create your views here.
def home (request): 
    produtoData = produto.objects.order_by('id')
    context = {'produto': produtoData}
    return render(request,'home.html',context)