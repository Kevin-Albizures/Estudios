import os
from colorama import Fore
from Metodos  import  CambiarEstadoActivo, lectura_XML_1,Limpiar_sistema,CrearEmpresa,lectura_XML_2,MostrarMenú2,CambiarEstadoInactivo,AtenderCliente,retirarCliente,LlenarEscritorios,simularAtención,VerEstadoAtencion,grafica

#----------------------------------------- Variables Globales-----------------------------------------
Empresa=None
Punto=None
Operación=0 # variable para elegir opción del menú
Salida=1
#----------------------------------------- Métodos y Funciones -----------------------------------------
#Limpiar la consola
def refrescarPantalla():
    os.system("cls")

#submenús:
# 1
def submenu1():
    Salida1=1
    refrescarPantalla()
    while Salida1==1:
        print("")
        print(Fore.LIGHTBLUE_EX+" .-.-.-.-. "+"\""+Fore.LIGHTCYAN_EX+"Soluciones Guatemaltecas, S.A."+Fore.LIGHTBLUE_EX+"\""+              " .-.-.-.-. ")
        print(Fore.LIGHTBLUE_EX+"|                                                    "                                                             +"|")
        print(Fore.LIGHTBLUE_EX+"|             "+Fore.LIGHTBLUE_EX+"Configuración de empresa               "                      +Fore.LIGHTBLUE_EX+"|")
        print(Fore.LIGHTBLUE_EX+"|                                                    "                                           +Fore.LIGHTBLUE_EX+"|")
        print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"1."+Fore.LIGHTCYAN_EX+" Crear nueva empresa                           "+Fore.LIGHTBLUE_EX+"|")
        print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"2."+Fore.LIGHTCYAN_EX+" Cargar archivo de configuración del sistema   "+Fore.LIGHTBLUE_EX+"|")
        print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"3."+Fore.LIGHTCYAN_EX+" Cargar archivo de configuración inicial       "+Fore.LIGHTBLUE_EX+"|")
        print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"4."+Fore.LIGHTCYAN_EX+" Limpiar sistema                               "+Fore.LIGHTBLUE_EX+"|")
        print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"5."+Fore.LIGHTCYAN_EX+" Regresar                                      "+Fore.LIGHTBLUE_EX+"|")
        print(Fore.LIGHTBLUE_EX+"|                                                    "                                                             +"|")
        print(Fore.LIGHTBLUE_EX+" -.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.- ")
        print(Fore.LIGHTCYAN_EX+"Ingrese el número de opción: ",end=" ")
        print("")
        Operación = input(Fore.LIGHTWHITE_EX+"")
        if Operación=="1":
            refrescarPantalla()
            CrearEmpresa()
        elif Operación=="2":
            lectura_XML_1()
            refrescarPantalla()
        elif Operación=="3":
            refrescarPantalla()
            print("")
            lectura_XML_2()
            refrescarPantalla()
        elif Operación=="4":
            refrescarPantalla()
            Limpiar_sistema()
        elif Operación=="5":
            Salida1=0
            refrescarPantalla()
        else:
            refrescarPantalla()
            input(Fore.LIGHTRED_EX+"Ingrese una opción válida.")
            refrescarPantalla()

# 2
def submenu2():
    global Empresa,Punto
    Empresa,Punto=MostrarMenú2()
    if Punto!=None:
        print("Código Empresa: "+Empresa.IdEmpresa)
        input("Código Punto de Atención: "+Punto.IdPuntoA)
        refrescarPantalla()

# 3
def submenu3():
    global Empresa,Punto
    Salida2=1
    refrescarPantalla()
    try:
        if Empresa!=None:
            Punto.CantClientes2=Punto.CantClientes
            LlenarEscritorios(Empresa,Punto)
        
            while Salida2==1:
                print("")
                print(Fore.LIGHTBLUE_EX+"   Empresa: "+"\""+Fore.LIGHTCYAN_EX+Empresa.Nombre+Fore.LIGHTBLUE_EX+"\"")
                print(Fore.LIGHTBLUE_EX+"   Punto de Atención: "+Fore.LIGHTCYAN_EX+Punto.Nombre+Fore.LIGHTCYAN_EX)
                print(Fore.LIGHTBLUE_EX+" ____________________________________________________ ")
                print(Fore.LIGHTBLUE_EX+"|                                                    "                                                             +"|")
                print(Fore.LIGHTBLUE_EX+"|           "+Fore.LIGHTBLUE_EX+"Manejo De Puntos De Atención             "                      +Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|                                                    "                                           +Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"1."+Fore.LIGHTCYAN_EX+" Ver estado del punto                          "+Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"2."+Fore.LIGHTCYAN_EX+" Activar escritorio de servicio                "+Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"3."+Fore.LIGHTCYAN_EX+" Desactivar escritorio                         "+Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"4."+Fore.LIGHTCYAN_EX+" Atender Cliente                               "+Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"5."+Fore.LIGHTCYAN_EX+" Solicitar atencion                            "+Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"6."+Fore.LIGHTCYAN_EX+" Simular actividad del punto de atención       "+Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"7."+Fore.LIGHTCYAN_EX+" Regresar                                      "+Fore.LIGHTBLUE_EX+"|")
                print(Fore.LIGHTBLUE_EX+"|                                                    "                                                             +"|")
                print(Fore.LIGHTBLUE_EX+" -.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.- ")
                print(Fore.LIGHTCYAN_EX+"Ingrese el número de opción: ",end="")
                Operación = input(Fore.LIGHTWHITE_EX+"")
                if Operación=="1":
                    VerEstadoAtencion(Empresa,Punto)
                    grafica(Empresa,Punto)
                elif Operación=="2":
                    CambiarEstadoInactivo(Empresa,Punto)
                elif Operación=="3":
                    CambiarEstadoActivo(Empresa,Punto)
                elif Operación=="4":
                    refrescarPantalla()
                    retirarCliente(Empresa,Punto)
                    grafica(Empresa,Punto)
                elif Operación=="5":
                    refrescarPantalla()
                    AtenderCliente(Empresa,Punto)
                elif Operación=="6":
                    refrescarPantalla()
                    simularAtención(Empresa,Punto)
                elif Operación=="7":
                    Salida2=0
                    refrescarPantalla()
                else:
                    refrescarPantalla()
                    input(Fore.LIGHTRED_EX+"Ingrese una opción válida.")
                    refrescarPantalla()
        else:
            print(Fore.RED+"Seleccione una empresa y una sucursal antes.")
    except AttributeError:
        return

#--------------------------------------------------------------------- Menú ---------------------------------------------------------------------
while Salida==1:
    print("")
    print(Fore.LIGHTBLUE_EX+" .-.-.-. "+"\""+Fore.LIGHTCYAN_EX+"Soluciones Guatemaltecas, S.A."+Fore.LIGHTBLUE_EX+"\""+              " .-.-.-. ")
    print(Fore.LIGHTBLUE_EX+"|                                                "                                                             +"|")
    print(Fore.LIGHTBLUE_EX+"|                      "+Fore.LIGHTBLUE_EX+"MENU                      "                      +Fore.LIGHTBLUE_EX+"|")
    print(Fore.LIGHTBLUE_EX+"|                                                "                                           +Fore.LIGHTBLUE_EX+"|")
    print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"1."+Fore.LIGHTCYAN_EX+" Configuración de empresa                  "+Fore.LIGHTBLUE_EX+"|")
    print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"2."+Fore.LIGHTCYAN_EX+" Selección de empresa y punto de atención  "+Fore.LIGHTBLUE_EX+"|")
    print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"3."+Fore.LIGHTCYAN_EX+" Manejo de puntos de atención              "+Fore.LIGHTBLUE_EX+"|")
    print(Fore.LIGHTBLUE_EX+"|   "+Fore.LIGHTWHITE_EX+"4."+Fore.LIGHTCYAN_EX+" Salir                                     "+Fore.LIGHTBLUE_EX+"|")
    print(Fore.LIGHTBLUE_EX+"|                                                "                                                             +"|")
    print(Fore.LIGHTBLUE_EX+" -.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.- ")
    print(Fore.LIGHTCYAN_EX+"Ingrese el número de opción: ",end="")
    Operación = input(Fore.LIGHTWHITE_EX+"")
    if Operación=="1":
        submenu1()
    elif Operación=="2":
        submenu2()
    elif Operación=="3":
        submenu3()
    elif Operación=="4":
        refrescarPantalla()
        input(Fore.RED+"Ha salido del programa D:")
        Salida=0

    elif Operación=="5":
        input("")

    else:
        refrescarPantalla()
        print(Fore.RED+"Ingrese una opción válida."+Fore.LIGHTWHITE_EX+"")