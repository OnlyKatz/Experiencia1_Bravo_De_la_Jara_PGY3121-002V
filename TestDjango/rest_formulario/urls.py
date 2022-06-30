from django.urls import path
from rest_formulario.views import lista_formularios, detalle_formulario
urlpatterns = [
    path('lista_formularios', lista_formularios, name="lista_formularios"),
    path('detalle_formulario/<id>', detalle_formulario, name="detalle_formulario"),

]