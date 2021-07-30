from django import forms
from personas.models import Persona
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PersonaForm, RawPersonaForm

from django.shortcuts import render
from django.views.generic.list import (
    ListView,
)
from .models import Persona

# Create your views here.
class PersonaListView(ListView):
    model = Persona


def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto':obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    initialValues = {
        'nombres' : 'Sin Nombre',
    }
    form = PersonaForm(request.POST or None, initial = initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form' : form
    }
    return render(request,'personas/personasCreate.html', context)

def personasAnotherCreateView(request):
    form = RawPersonaForm()#request.GET
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data) #grabar datos
        else:
            print(form.errors)
    context = {
        'form' : form,
    }
    return render(request, 'personas/PersonasCreate.html', context)

def personasShowObject(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    context ={
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    if request.method == "POST":
        print("lo borro")
        obj.delete()
        return redirect('../')
    context = {
        'objeto' : obj,
    }
    return render(request, 'personas/personasBorrar.html', context)

def personasListView(request):
    queryset = Persona.objects.all()
    context = {
        'objectList':queryset,
    }
    return render(request, 'personas/personasLista.html', context)