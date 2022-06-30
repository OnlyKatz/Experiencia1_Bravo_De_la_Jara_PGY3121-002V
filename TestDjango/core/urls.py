
from xml.etree.ElementInclude import include
from django.urls import path
from .import views
from .views import mostrar


urlpatterns = [
    path('', views.home, name="home"),
    path('galeria/', views.galeria, name="galeria"),
    path('somos/', views.somos, name="somos"),
    path('formulario/', views.formulario, name="formulario"),
    path('mostrar/', views.mostrar, name="mostrar"),
    path('mod_form/<id>', views.mod_form, name="mod_form"),
    path('del_form/<id>', views.del_form, name="del_form"),
    path('egg/', views.egg, name="egg"),
    path('consumo', views.consumo, name="consumo")
    
]