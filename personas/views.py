from personas.models import Persona
from django.shortcuts import render

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'nombre' : obj.nombres,
        'edad' : obj.edad,
    }
    return render(request, 'personas/test.html', context)