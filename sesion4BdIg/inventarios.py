#sistema de inventarios   gestion mercancias

#lista registrosPoductos
registrosProductos=[]#lista vacia para esperar valores y es una lista acumuladora

while True:
    print('MENU INVENTARIOS TIENDAS TOVAR\n(1) Ingresar articulo\n(2) Consultar articulo\n(3) Comprar articulo\n(4) Vender articulo\n(5) Salir\n')
    opc=str(input('Capture un numero del 1 - 5:'))
    if(opc=='1'):
        print('--------------MODULO DE ALTAS PRODUCTOS---------------------')
        codProducto=int(input('Capture codigo producto:'))
        cantProducto = int(input('Capture cantidad producto:'))
        precioProducto=float(input('Capture precio producto:'))
        nombreProducto=input('Ingrese Nombre Producto:')
        #para guardar los valores antes ingresados   en lista "registrosProd" para cada fila de datos
        registrosProd=[codProducto,cantProducto,precioProducto,nombreProducto]#guarda solo datos de una fila
        registrosProductos=registrosProductos+[registrosProd]#Acumula los datos de los articulos registrados
    elif(opc=='2'):
        print('MODULO DE CONSULTA POR CODIGO PRODUCTOS')
        consultar = int(input('Ingrese codigo de producto para busqueda:'))#Campo distintivo
        p = -1;
        for i in range(len(registrosProductos)):
            if consultar == registrosProductos[i][0]:
                p = i
                break
        if p < 0:
            print('Articulo no existe')
        else:
            print('Cantidad : ', registrosProductos[p][1])
            print('Precio : ', registrosProductos[p][2])
            print('Nombre : ', registrosProductos[p][3])
    elif (opc == '3'):
        print('MODULO DE COMPRAS PROVEEDOR PRODUCTOS')
        c=int(input('Ingrese codigo producto :'))
        p=-1;
        for i in range(len(registrosProductos)):
            if c==registrosProductos[i][0]:
                p=i
                break
        if p<0:
            print('Articulo no existe')
        else:
            k=int(input('Ingrese la cantidad comprada :'))
            registrosProductos[p][1]=registrosProductos[p][1]+k
            print('Usted ha hecho una compra de : ',k)
            print('verifique su consulta')
    elif (opc == '4'):
        print('MODULO DE VENTAS PRODUCTOS')
        c = int(input('Ingrese codigo producto :'))
        p = -1;
        for i in range(len(registrosProductos)):
            if c == registrosProductos[i][0]:
                p = i
                break
        if p < 0:
            print('Articulo no existe')
        else:
            k = int(input('Ingrese la cantidad vendida :'))
            registrosProductos[p][1] = registrosProductos[p][1] - k
            print('Usted ha hecho una VENTA de : ', k)
            print('verifique su consulta')
    elif (opc == '5'):
        print('HA FINALIZADO PROGRAMA')
        break
    else:
        print('OPCION SOLO TENGO 1,2,3,4,5')