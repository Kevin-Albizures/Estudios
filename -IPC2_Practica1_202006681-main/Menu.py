import os
from colorama import Fore
from CrearLista import ListaPedidos,N 

# Variables para el menú
OpcMenú=0
# Condición para salir
salir=1
# Condición para inicializar la lista:
EstaVacía=0
N=0

PedidosLista=ListaPedidos()
# Borrar consola
def refrescarPantalla():
    os.system("cls")

def añadirOrden():
    global PedidosLista
    refrescarPantalla()
    print(Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"¡Vamo' a preparar!"+Fore.LIGHTYELLOW_EX+" -----------------")
    nom=input(Fore.LIGHTGREEN_EX+   "Nombre del cliente: "+ Fore.LIGHTYELLOW_EX)
    dir=input(Fore.LIGHTGREEN_EX+   "Dirección: "+          Fore.LIGHTYELLOW_EX)
    NIT=input(Fore.LIGHTGREEN_EX+   "NIT: "+                Fore.LIGHTYELLOW_EX)
    print(Fore.LIGHTBLUE_EX+  "  Formas de pago: ")
    print(Fore.LIGHTBLUE_EX+  "    1. Tarjeta")
    print(Fore.LIGHTBLUE_EX+  "    2. Efectivo")
    v=input(Fore.LIGHTGREEN_EX+  "Ingresar forma de pago: "+      Fore.LIGHTYELLOW_EX)
    if v=="1":
        Pago="Tarjeta"
    elif v=="2":
        Pago="Efectivo"
    else:
        refrescarPantalla()
        input(Fore.RED+"Ingrese una forma de pago válida. ")
        return
    print(Fore.LIGHTBLUE_EX+       " Lista de ingredientes: ")
    print(Fore.LIGHTBLUE_EX+        "     1. Salchicha - 2 min")
    print(Fore.LIGHTBLUE_EX+        "     2. Chorizo - 3 min")
    print(Fore.LIGHTBLUE_EX+        "     3. Salami - 1.5 min")
    print(Fore.LIGHTBLUE_EX+        "     4. Longaniza - 4 min")
    print(Fore.LIGHTBLUE_EX+        "     5. Costilla - 6 min")
    ing=input(Fore.LIGHTGREEN_EX+   "Igrediente: "+     Fore.LIGHTYELLOW_EX)
    cant=input(Fore.LIGHTGREEN_EX+  "Cantidad: "+       Fore.LIGHTYELLOW_EX)
    if ing=="1":
        tiempo=2*int(cant)
    elif ing=="2":
        tiempo=3*int(cant)
    elif ing=="3":
        tiempo=1.5*int(cant)
    elif ing=="4":
        tiempo=4*int(cant)
    elif ing=="5":
        tiempo=6*int(cant)
    else:
        refrescarPantalla()
        input(Fore.RED+"Opción no válida de ingrediente. ")
        return
    PedidosLista.agregarAListaUltimo(nom,dir,NIT,Pago,ing,tiempo,cant)
    PedidosLista.grafica()

    print(Fore.LIGHTYELLOW_EX+"¿Desea ingresar otro tipo de ingrediente? ")
    v2=input("Si/NO  ")
    if v2=="Si" or v2=="si" or v2=="SI":
        print(Fore.LIGHTBLUE_EX+        " Lista de ingredientes: ")
        print(Fore.LIGHTBLUE_EX+        "     1. Salchicha - 2 min")
        print(Fore.LIGHTBLUE_EX+        "     2. Chorizo - 3 min")
        print(Fore.LIGHTBLUE_EX+        "     3. Salami - 1.5 min")
        print(Fore.LIGHTBLUE_EX+        "     4. Longaniza - 4 min")
        print(Fore.LIGHTBLUE_EX+        "     5. Costilla - 6 min")
        ing=input(Fore.LIGHTGREEN_EX+   "Igrediente: "+     Fore.LIGHTYELLOW_EX)
        cant=input(Fore.LIGHTGREEN_EX+  "Cantidad: "+       Fore.LIGHTYELLOW_EX)
        if ing=="1":
            tiempo=2*int(cant)
        elif ing=="2":
            tiempo=3*int(cant)
        elif ing=="3":
            tiempo=1.5*int(cant)
        elif ing=="4":
            tiempo=4*int(cant)
        elif ing=="5":
            tiempo=6*int(cant)
        else:
            refrescarPantalla()
            input(Fore.RED+"Opción no válida de ingrediente. ")
            return
        PedidosLista.agregarAListaUltimo(nom,dir,NIT,Pago,ing,tiempo,cant)
        PedidosLista.grafica()
    refrescarPantalla()

def EliminarOrden():
    global PedidosLista
    refrescarPantalla()
    PedidosLista.eliminar_inicio()
    refrescarPantalla()

def RevisarOrden():
    global PedidosLista
    refrescarPantalla()
    print("")
    PedidosLista.recorrerInicio_Fin()
    refrescarPantalla()

refrescarPantalla()
# Ciclo para que no permita terminar el programa
while salir==1:
    print("")
    print(Fore.LIGHTYELLOW_EX+" .-.-.-.-"+"\""+Fore.BLUE+"HOT DOG LOS PERRONES"+Fore.LIGHTYELLOW_EX+"\""+"-.-.-.-. ")
    print(Fore.LIGHTGREEN_EX+ "|                                      "                                             +Fore.LIGHTYELLOW_EX+"|")
    print(Fore.LIGHTYELLOW_EX+"|                 "+Fore.BLUE+"Menú                 "                                 +Fore.LIGHTGREEN_EX+"|")
    print(Fore.LIGHTGREEN_EX+ "|                                      "                                             +Fore.LIGHTYELLOW_EX+"|")
    print(Fore.LIGHTYELLOW_EX+"|      "+Fore.LIGHTGREEN_EX+"1."+Fore.LIGHTYELLOW_EX+" Añadir orden                 " +Fore.LIGHTGREEN_EX+"|")
    print(Fore.LIGHTGREEN_EX+ "|      "+Fore.LIGHTGREEN_EX+"2."+Fore.LIGHTYELLOW_EX+" Retirar orden                "+Fore.LIGHTYELLOW_EX+"|")
    print(Fore.LIGHTGREEN_EX+ "|      "+Fore.LIGHTGREEN_EX+"3."+Fore.LIGHTYELLOW_EX+" Revisar ordenes              "+Fore.LIGHTYELLOW_EX+"|")
    print(Fore.LIGHTYELLOW_EX+"|      "+Fore.LIGHTGREEN_EX+"4."+Fore.LIGHTYELLOW_EX+" Datos del desarrollador      " +Fore.LIGHTGREEN_EX+"|")
    print(Fore.LIGHTYELLOW_EX+"|      "+Fore.LIGHTGREEN_EX+"5."+Fore.LIGHTYELLOW_EX+" Salir                        " +Fore.LIGHTGREEN_EX+"|")
    print(Fore.LIGHTGREEN_EX+ "|                                      "                                             +Fore.LIGHTYELLOW_EX+"|")
    print(Fore.LIGHTYELLOW_EX+" -.-.-.-.-.-.-.-.-__-.-.-.-.-.-.-.-.-.- ")
    OpcMenú = input(Fore.LIGHTGREEN_EX+"Ingrese el número de opción: ")

    if OpcMenú=="1":
        añadirOrden()
    elif OpcMenú=="2":
        EliminarOrden()
    elif OpcMenú=="3":
        RevisarOrden()
    elif OpcMenú=="4":
        refrescarPantalla()
        print(Fore.LIGHTBLUE_EX+"__________________Datos__________________")
        print(Fore.LIGHTYELLOW_EX+"Nombre: Kevin Haroldo Albizures Sirín")
        print(Fore.LIGHTYELLOW_EX+"Carnet: 202006681")
        print(Fore.LIGHTYELLOW_EX+"País: Guatemala")
        print(Fore.LIGHTYELLOW_EX+"Correo: ks.albizures@gmail.com")
        input("")
        refrescarPantalla()
    elif OpcMenú=="5":
        salir=0
    else:
        input(Fore.LIGHTRED_EX+"No tenemos esa opción. :( ")
        refrescarPantalla()

print(Fore.LIGHTBLUE_EX+"Programa finalizado con éxito :) "+Fore.LIGHTWHITE_EX)