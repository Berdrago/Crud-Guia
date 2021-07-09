from app.views import agregar, editar, eliminar, index
from django.urls import path

urlpatterns = [
    path('', index ,  name='index'),#Nueva ruta 
    path('agregar/', agregar, name='agregar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
    
]
