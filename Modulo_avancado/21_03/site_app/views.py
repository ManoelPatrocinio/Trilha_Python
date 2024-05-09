from django.shortcuts import render
from site_app.models import *
from site_app.forms import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout as authLogout
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username e senha recebida", username,password)
        
        user = authenticate(username=username, password=password)
        print("status do user",user)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else: 
            form.add_error(None, "Credenciais inválidas. Por favor, tente novamente.")
    else:
        print("requisição do tipo get")
        form = SignIn_form()
        
    context = {'form_signIn':form}
    return render(request,'login.html',context)

def logout(request):
    authLogout(request)
    return HttpResponseRedirect(reverse('home'))
    
def page_registro (request): 
    if request.method == "POST":
        form = SignUp_form(request.POST)
        if form.is_valid():
            if request.POST.get('id_user_confirme_password') != request.POST.get('password'):
              form.add_error("password","As senha precisam ser iguais")  
            else:
                post = form.save(commit=False)
                post.password = make_password(post.password)
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

def removeAccount(request):

    if request.user.is_authenticated:
        try:
            userData = Usuario.objects.get(id=request.user.id)
            userData.delete()
            authLogout(request)
        except Usuario.DoesNotExist:
            # caso em que o usuário não existe
            print("sem usuario com esse ID")
            return HttpResponseRedirect(reverse('home'))
            
    return HttpResponseRedirect(reverse('home'))
    
def page_about(request):
    return render(request,'sobre.html')

def page_registerCategory(request):
    if request.method == "POST":
        form = Catagoria_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('home'))           
    else:
        form = Catagoria_form()
        
    context = {'form_addCategoria':form}
    return render(request,'registro_categoria.html',context)

def page_editperfil (request):
    if request.method == 'POST':
        usuario = User.objects.get(id=request.user.id)
        novo_usuario = request.POST.copy()
        
        novo_usuario['password'] = usuario.password
        novo_usuario['username'] = usuario.username
        
        user = SignUp_form(instance=usuario, data=novo_usuario)
        if user.is_valid:
            user.save()
    else:        
        if request.user.is_authenticated:
            context = {
                'formEdit' : SignUp_form(),
            }
            context['formEdit'] = SignUp_form(instance=User.objects.get(id=request.user.id))
            text = User.objects.get(id=request.user.id)
            print("get user", context)
            
            return render(request,"edit_user.html",context) 
        else:
            return HttpResponseRedirect(reverse('home'))


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

