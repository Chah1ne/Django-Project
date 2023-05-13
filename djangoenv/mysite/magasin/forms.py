from django import forms
#class FrsForm(forms.Form):
 #   nom=forms.CharField(max_length=30)
  #  adr=forms.CharField(widget=forms.Textarea)
   # email=forms.EmailField()
    #tel=forms.CharField(max_length=8)
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class ProduitForm (ModelForm ):
    class Meta :
        model = produit
        fields = "__all__"
        #fields=['libelle','description']
class FournisseurForm (ModelForm):
    class Meta :
        model = fournisseur 
        fields = "__all__"
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')