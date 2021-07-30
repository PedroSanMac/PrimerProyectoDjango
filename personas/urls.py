from personas.models import Persona
from django.urls import path
from personas.views import (
    PersonaDetailView,
    PersonaListView,
    PersonaCreateView,
    PersonaUpdateView,
    PersonaDeleteView,
 )
from personas.views import (
    personaTestView,
    personaCreateView,
    personasAnotherCreateView,
    personasDeleteView, personasListView, personasShowObject
)

app_name= 'personas'

urlpatterns =[
    path('agregar/', personaCreateView, name='CreatePersona'),
    path('anotherAdd', personasAnotherCreateView, name='OtroAgregarPersonas'),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID>/borrar/', personasDeleteView, name='deleting'),
    #path('', personasListView, name='listing')

    path('', PersonaListView.as_view(), name= 'persona-list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
    path('create/', PersonaCreateView.as_view(), name = 'persona-create'),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name='persona-update'),
    path('<int:pk>/delete/', PersonaDeleteView.as_view(), name='persona-delete'),
]