from conn import ConexionPG
import os
import sys

############# CONEXION CON BASE DE DATOS ################
def main():
    conexion_pg = ConexionPG(
        direccion_servidor='127.0.0.1', # O localhost
        usuario='postgres',
        contrasenia='Ar2098urd',
        base_datos='reto2'
    )
    
    conexion_pg.crear_tabla()
    conexion_pg.crear_tabla_clientes()
    menu_comprador(conexion_pg)
    menu_administrador(conexion_pg)
    
    
    

############ FUNCION PARA AGREGAR LOS ARTICULOS """ALMACEN"""" ################
def agregar_articulos_almacen(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_articulos(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

############ FUNCION PARA AGREGAR LOS ARTICULOS """CLIENTES"""" ################
def agregar_articulos_clientes(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Shop******\n")
        print("*****Articulos en lista******\n")
        print("--  -------   -------------------------------    ----- -------------")
        print("ID  nombre                 fecha                 cant.    precio") 
        print("--  -------   -------------------------------    ----- -------------")    
        print(conexion_pg.ver_articulos())     

        articulo = input("\nIngrese el nombre del articulo: ")
        cantidad = int(input("\ncuantos son?: "))
        precio = float(input("\ncuanto cuesta?: "))
        subtotal = float(precio + cantidad)
        igv = float(subtotal * 0.18)
        total = float(subtotal + igv)

        conexion_pg.insertar_articulos_clientes(articulo, cantidad, subtotal, igv, total)
        
        print("ARTICULO AGREGADO!!!\n")
        print("el total a pagar es: ", total)
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")    
   

############# FUNCION PARA VER LOS ARTICULOS """CLIENTES""" ################
def ver_articulos(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Articulos en carrito******\n")
        print("--- --------- -------------------------------    ----- -------------   ---------------- -----------------")
        print("nro articulo               fecha                 cant.    subtotal            igv        total a pagar") 
        print("--- --------- -------------------------------    ----- -------------   ---------------- -----------------")    
        print(conexion_pg.ver_articulos_clientes())     
    
        print('\n[m] Para regresar al menu principal')
        print('\n[s] Para salir')
        opcion = input("\nElija una opcion: ")
        
        if opcion == "m":
            continuar = False
            os.system("clear")
        elif opcion == "s":
            sys.exit()
        else:
            opcion == input("\nDigite una seleccion valida: ")

############# FUNCION PARA ELIMINAR ARTICULOS """CLIENTES""" ################
def eliminar_articulo_clientes(conexion_pg):
    continuar = True
    os.system("clear")


    print("*****Elimina el articulos con su nro******\n")
    print("*****Articulos en carrito******\n")
    print("--- --------- -------------------------------    ----- -------------   ---------------- -----------------")
    print("nro articulo               fecha                 cant.    subtotal            igv        total a pagar") 
    print("--- --------- -------------------------------    ----- -------------   ---------------- -----------------")    
    print(conexion_pg.ver_articulos_clientes())

    eliminate = input('\nIntroduce el nro del producto: ')
    pregunta = input('\nEstas seguro que quieres eliminarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.eliminar_articulo_usuarios(eliminate)
        print("ARTICULO ELIMINADO!!!")
    elif pregunta == "n":
        continuar = False

    
    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

############# FUNCION PARA ELIMINAR ARTICULOS """ALMACEN""" ################
def eliminar_articulo(conexion_pg):
    continuar = True
    os.system("clear")


    print("*****Elimina el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_articulos())

    eliminate = input('\nIntroduce el ID del producto: ')
    pregunta = input('\nEstas seguro que quieres eliminarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.eliminar_articulo_almacen(eliminate)
        print("ARTICULO ELIMINADO!!!")
    elif pregunta == "n":
        continuar = False

    
    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

############ FUNCION PARA MODIFICAR ARTICULOS """ALMACEN""" ###############
def modificar_articulo_almacen(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_articulos())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_articulos(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

###################### MENU PRINCIPAL #######################
def menu_comprador(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("""\t\t\t© Store Hackathon
        \t\t█║▌│█│║▌║││█║▌║▌║\n""")
        print("***************************BIENVENIDO***************************\n")
        print('SI DESEA COMPRAR NUESTROS PORDUCTOS EN STOCK DIGITE "1"\n')
        print('[1] Comprar articulos')
        print('[0] Ver articulos a pagar')
        print('[d] Eliminar articulos a pagar')
        print('[a] Administrador')
        print('\n[s] Salir')
        print("\n**************************************************************\n")
        opcion = input('Digite su seleccion: ')
    
        if opcion == "1":
            agregar_articulos_clientes(conexion_pg)
        elif opcion == "0":
            ver_articulos(conexion_pg)
        elif opcion == "d":
            eliminar_articulo_clientes(conexion_pg)
        elif opcion == "a":
            menu_administrador(conexion_pg)
        elif opcion == "s":
            sys.exit()
        else:
            opcion == input("elija una seleccion valida: ")

###################### MENU ADMINISTRADOR #######################        
def menu_administrador(conexion_pg):
    os.system("clear")
    continuar = True
    while continuar:
        print("\n**********ADMINISTRADOR**********\n")
        print('[1] Agregar articulos al almacen')
        print('[2] Ver articulos en almacen')
        print('[3] Modificar articulos en el almacen')
        print('[4] Eliminar articulos del almacen')
        print('\n[s] Salir del sistema')
        print("\n**********************************\n")
        opcion = input('Digite su seleccion: ')
        

        if opcion == "1":
            agregar_articulos_almacen(conexion_pg)
        elif opcion == "2":
            ver_articulos(conexion_pg)
        elif opcion == "3":
            modificar_articulo_almacen(conexion_pg)
        elif opcion == "4":
            eliminar_articulo(conexion_pg)
        elif opcion == "s":
            sys.exit()
        else:
            opcion == input("elija una seleccion valida: ")
#########################################################################

main()