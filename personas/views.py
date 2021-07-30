from django import forms
from django.db.models import fields
from django.http.response import JsonResponse
from django.views.generic.base import View
from django.http import HttpResponse
from personas.models import Persona
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PersonaForm, RawPersonaForm

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Persona

# Create your views here.
class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__lte='18')

class PersonaDetailView(DetailView):
    model = Persona


class PersonaCreateView(CreateView):
    model = Persona
    fields =[
        'nombres',
        'apellidos',
        'edad',
        'donador',
    ]

class PersonaUpdateView(UpdateView):
    model = Persona
    fields =[
        'nombres',
        'apellidos',
        'edad',
        'donador',
    ]
class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas:persona-list')

class PersonaQueryView(View):
    def get(self, request, *args, **kwargs):
        queryset = Persona.objects.filter(edad__lte='40')
        return JsonResponse(list(queryset.values()), safe=False)

#--------------------------------------------------------------------------
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