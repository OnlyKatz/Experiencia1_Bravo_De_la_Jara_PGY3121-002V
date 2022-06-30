from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Formulario 
from .serializers import FormularioSerializer
from django.core.exceptions import ObjectDoesNotExist
@csrf_exempt
@api_view(['GET','POST'])
def lista_formularios(request):

    if request.method == 'GET':
        formulario = Formulario.objects.all()
        serializer = FormularioSerializer(formulario,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FormularioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_formulario(request, id):

    try:
        formulario = Formulario.objects.get(correo=id)
    except Formulario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FormularioSerializer(formulario)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FormularioSerializer(formulario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            formulario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

         




# Create your views here.
