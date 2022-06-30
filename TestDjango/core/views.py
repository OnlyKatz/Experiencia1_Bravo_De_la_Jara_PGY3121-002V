from xml.dom.expatbuilder import ExpatBuilderNS
from django.shortcuts import redirect, render
from .models import Vehiculo, Formulario
from .forms import ContactoForm

# Create your views here.

def home(request):

    vehiculos = Vehiculo.objects.all()
    formularios = Formulario.objects.all()

    datos={
        'vehiculos':vehiculos,
        'formularios':formularios
    }

    return render(request, 'core/home.html', datos)
    
def galeria(request):
    return render(request, 'core/galeria.html',)

def somos(request):
    return render(request, 'core/somos.html',)

def formulario(request):
    if request.method=='POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect(to='formulario')
    else:
        contacto_form = ContactoForm()
    return render(request, 'core/formulario.html', {'contacto_form': contacto_form})



def mostrar(request):
    formularios = Formulario.objects.all()

    datos={
        'formularios':formularios
    }

    return render(request, 'core/mostrar.html', datos)


def mod_form(request, id):

    formularios = Formulario.objects.get(correo=id)
    datos = {
        'form': ContactoForm(instance=formularios)
    }
    if request.method=='POST':
        formulario = ContactoForm(data = request.POST, instance=formularios)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrar')
    return render(request, 'core/mod_form.html', datos )

def del_form(request, id):
    formulario = Formulario.objects.get(correo=id)
    formulario.delete()
    return redirect ('mostrar')

def egg(request):
    return render(request, 'core/EasterEgg.html',)

def consumo(request):
    return render(request, 'core/consumo.html',)