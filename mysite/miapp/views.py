from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Producto
# Create your views here.

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        disponibilidad = request.POST.get('disponibilidad') == 'on'

        Producto.objects.create(
            nombre=nombre,
            decripcion=descripcion,
            precio=precio,
            disponibilidad=disponibilidad
        )

        return redirect('agregar_productos') 
    return render(request, 'agregar_producto.html')

def lista_productos(request):
    productos = list(Producto.objects.values())
    return JsonResponse(productos, safe=False)

def obtener_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return JsonResponse({
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.decripcion,
        'precio': str(producto.precio),
        'disponibilidad': producto.disponibilidad
    })


def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.decripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.disponibilidad = request.POST.get('disponibilidad') == 'on'
        producto.save()

        return redirect('lista_productos')

    return render(request, 'agregar_producto.html', {'producto':producto, 'modo':'modificar'})

def eliminar_producto(request, producto_id):
    mi_producto = Producto.objects.get(id = producto_id)
    mi_producto.delete()
    return redirect('lista_productos')
