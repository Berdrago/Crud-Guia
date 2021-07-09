
from app.models import Sistema, Smartphone
from django.shortcuts import redirect, render

# Create your views here.


#Funcion para renderizar el html
def index(request):

    smartphones = Smartphone.objects.all() #Se traean todos los datos de la tabla
    sistemas = Sistema.objects.all()

    contexto = { 'smartphones' : smartphones, 'sistemas': sistemas}
    return render(request, 'index.html',contexto)

def agregar(request):
    modelo = request.POST.get('modelo', '')
    id_sistema  = request.POST.get('sistema', '')

    sistema = Sistema.objects.get(id = id_sistema)

    smartphone = Smartphone(modelo = modelo, sistema = sistema )
    smartphone.save()

    return  redirect('index')
def editar(request, id ):
    modelo = request.POST.get('modelo','')
    id_sistema  = request.POST.get('sistema', '')

    sistema = Sistema.objects.get(id = id_sistema)

    smartphone = Smartphone.objects.get(id = id )

    smartphone.modelo = modelo
    smartphone.sistema = sistema
    
    smartphone.save()
    return redirect('index')    
def eliminar(request, id):
    smartphone =Smartphone.objects.get(id = id )
    smartphone.delete()

    return redirect('index')

    