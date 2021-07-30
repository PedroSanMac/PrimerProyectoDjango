from django.urls import path
from personas.views import personaTestView, personaCreateView, personasAnotherCreateView, personasDeleteView, personasListView, personasShowObject

app_name= 'personas'

urlpatterns =[
    path('agregar/', personaCreateView, name='CreatePersona'),
    path('anotherAdd', personasAnotherCreateView, name='OtroAgregarPersonas'),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID>/borrar/', personasDeleteView, name='deleting'),
    path('/', personasListView, name='listing')
]