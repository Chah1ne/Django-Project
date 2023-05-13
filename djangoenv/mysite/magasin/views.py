from django.http import HttpResponseRedirect
from .models import produit
from .forms import *
from django.shortcuts import redirect, render
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm


def index(request):
    list=produit.objects.all() 
    return render(request,'magasin/vitrine.html',{'list':list})

def AddProd(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()
    produits = produit.objects.all()
    return render(request, 'magasin/majProduits.html', {'produits': produits, 'form': form})

def produit_detail(request, product_id):
    # Récupérer le produit correspondant à l'identifiant unique donné
    product = get_object_or_404(produit, id=product_id)
    
    return render(request, 'product_detail.html', {'product': product})

def edit_product(request, product_id):
    produit = produit.objects.get(id=product_id)
    form = ProduitForm(instance=produit)
    
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit_detail', product_id=produit.id)
    
    return render(request, 'edit_produit.html', {'form': form, 'produit': produit})

def delete_product(request, pk):
    product = get_object_or_404(produit, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'magasin/delete_product.html', {'product': product})

    

def nouveauFournisseur(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES) 
        if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect('/magasin/affichefou') 
        else: 
            form = FournisseurForm() 
        fournisseurs=fournisseur.objects.all()
    return render(request,'magasin/testForm.html',{'fournisseurs':fournisseurs,'form':form})
def affichefou(request):
    fou=fournisseur.objects.all()
    return render(request,'magasin/vitrine2.html',{'fou':fou})
def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})