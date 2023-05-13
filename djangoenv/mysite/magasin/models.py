from django.db import models
from datetime import date
# Create your models here.

class produit(models.Model):
    TYPE_CHOICES=[
        ('em','emballé'),
        ('fr','Frais'),
        ('cs','Conserve')
    ]
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='Non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True,upload_to='media/')
    categorie=models.ForeignKey('categorie',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "libellé "+self.libellé+" description "+self.description+" prix "+str(self.prix)+" type "+self.type
class categorie(models.Model):
    TYPE_CHOICES=[
        ('al','alimentaire'),
        ('mb','meuble'),
        ('vs','vaisselle'),
        ('sn','sanitaire'),
        ('vt','vetement'),
        ('jx','jouets'),
        ('lg','linge de maison'),
        ('bj','bijoux'),
        ('dc','decor')

    ]
    libellé=models.CharField(default='al',choices=TYPE_CHOICES,max_length=50)
    def __str__(self):
        return self.libellé
class fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default='Non définie')
    email=models.EmailField(default='Non définie')
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom
class produitNC(produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return "libellé "+self.libellé+" description "+self.description+" prix "+str(self.prix)+" type "+self.type+" duree de garantie "+self.Duree_garantie
class command(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')	
