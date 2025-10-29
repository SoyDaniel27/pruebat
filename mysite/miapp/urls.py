from django.urls import path
from . import views

urlpatterns = [
    path('api/lista/productos', views.lista_productos, name='lista_productos'),
    path('api/agregar/productos', views.agregar_producto, name='agregar_productos'),
    path('api/obtener/producto/<int:producto_id>', views.obtener_producto, name='obtener_producto'),
    path('api/modificar/producto/<int:producto_id>', views.modificar_producto, name='modificar_producto'),
    path('api/eliminar/producto/<int:producto_id>', views.eliminar_producto, name='eliminar_producto')
]