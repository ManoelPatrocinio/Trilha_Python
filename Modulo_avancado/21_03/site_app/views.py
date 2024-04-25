from django.shortcuts import render
from site_app.models import Produto
from site_app.forms import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home (request): 
    produtoData = Produto.objects.order_by('id')
    context = {'produtos': produtoData} 
    return render(request,'home.html',context)

def page_roupas (request):
    produtoData = Produto.objects.order_by('id')
    context = {'produtos': produtoData} 
    return render(request,'roupas.html',context)

def page_roupa_detalhe(request, produto_id):
    produtoData = Produto.objects.get(id=produto_id)
    context = {'produto':produtoData}
    return render(request,'roupa_detalhe.html',context)


def page_login (request): 
    if request.method == "POST":
        form = SignIn_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignIn_form()
        
    context = {'form_signIn':form}
    return render(request,'login.html',context)

def page_registro (request): 
    if request.method == "POST":
        form = SignUp_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignUp_form()
        
    context = {'form_signUp':form}
    return render(request,'registro.html',context)

def page_registro_influencer (request): 
    if request.method == "POST":
        form = Influencer_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('registro_influencer'))
    else:
        form = Influencer_form()
        
    context = {'form_influencer':form}
    return render(request,'registro_influencer.html',context)


# Admin views

def page_registroProduto (request): 
    if request.method == "POST":
        form = Produto_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('createProduct')
    else:
        form = Produto_form()
        
    context = {'form_add':form}
    return render(request,'registroProduto.html',context)

