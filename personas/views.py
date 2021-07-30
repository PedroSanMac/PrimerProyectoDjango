from django import forms
from personas.models import Persona
from django.shortcuts import render
from .forms import PersonaForm, RawPersonaForm

# Create your views here.
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