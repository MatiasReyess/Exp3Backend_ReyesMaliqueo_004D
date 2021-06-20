from django.urls import path
from .views import index,galeria,mostrar,form_subir,modcomen,delete_comen

urlpatterns = [
    path('', index, name='index'),
    path('galeria/', galeria, name='galeria'),
    path('mostrar',mostrar,name='mostrar'),
    path('subir',form_subir,name="subir"),
    path('modcomen/<id>',modcomen, name="modcomen"),
    path('delete_comen/<id>',delete_comen,name="delete_comen")
]