from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('affichefou/',views.affichefou,name='affichefou'),
    path('edit_product/',views.edit_product,name='edit_product'),
    path('produit_detail/',views.produit_detail,name='produit_detail'),
    path('list/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('nouveauFournisseur/',views.nouveauFournisseur,name='nouveauFournisseur'),
    path('AddProd/',views.AddProd,name='AddProd'),
    path('register/',views.register, name = 'register'), 

]