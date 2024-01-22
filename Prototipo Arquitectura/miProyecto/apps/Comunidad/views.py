import json
from django.shortcuts import render, redirect
from .models import *
import os
from django.conf import settings
import requests
# Create your views here.



def Inicio(request):
    return render(request,'inicio.html')

def IniSesion(request):
    return render(request,'Sing-Login.html')

def Tienda(request):
    productos = Producto.objects.all()
    cate_producto_Interior = Producto.objects.filter(categoriaId = 1) 
    cate_producto_Exterior = Producto.objects.filter(categoriaId = 2) 
    cate_producto_Maseteros = Producto.objects.filter(categoriaId = 3) 
    return render(request,'Tienda.html',{"producto":productos,"cate_interior":cate_producto_Interior,"cate_exterior": cate_producto_Exterior,"cate_masetero": cate_producto_Maseteros})


def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregarProductos.html",{"cate":categorias,"prod":productos})


def agregarProducto(request):
    #print("AGREGAR PRODUCTOS", request.POST)

    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_imagen = request.FILES['txtImagen']

    Producto.objects.create(sku = v_sku, nombre = v_nombre, precio = v_precio,stock = v_stock, descripcion = v_descripcion, imagenUrl=v_imagen,categoriaId = v_categoria)
    
    return redirect('/agregarProducto')



def cargarEditarProducto(request,sku):
    prod = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()
    return render(request,"editarProducto.html",{"prod":prod, "cate":categorias})


def editarProducto(request):
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']


    try:
        v_imagen = request.FILES['txtImagen']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagenUrl))
        os.remove(ruta_imagen)
    except:
        v_imagen = productoBD.imagenUrl

    productoBD.nombre = v_nombre
    productoBD.precio = v_precio
    productoBD.stock = v_stock
    productoBD.descripcion = v_descripcion
    productoBD.categoriaId = v_categoria
    productoBD.imagenUrl = v_imagen
    
    productoBD.save()

    return redirect('/agregarProducto')



def eliminarProducto(request,codigo_producto):
    producto = Producto.objects.get(sku = codigo_producto)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagenUrl))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarProducto')


def prod(request):
    productos = Producto.objects.all()
    cate_producto_jardineria = Producto.objects.filter(categoriaId = 1) 
    cate_producto_arbol = Producto.objects.filter(categoriaId = 2) 
    return render(request,"prod.html",{"producto":productos,"cate_arbol":cate_producto_arbol,"cate_jardineria": cate_producto_jardineria})


URL_SALESFORCE='http://192.168.100.18:8003/api/sistema_bodega/v1/productos/?format=json'
def salesforce_productos(request):
    
    if request.method == 'GET':
        
        response = requests.get(
            URL_SALESFORCE
        )
        datos = response.json()
            
        context = {
            'productos': datos
        }
            
        # print(productos) 
        print(datos) 
        return render(request,'productos.html' , context) 
    
    elif request.method == 'POST':
        print(request.POST)
        
        productos = request.POST['productos.html']
        
        for id,p in enumerate(productos):
            print(f" PRODUCTO {id}   -> {p}")
        

