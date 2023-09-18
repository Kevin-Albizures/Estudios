import os
from asyncio.windows_events import NULL
import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog
from Clases import ListaEmpresa
from colorama import Fore
# Variables globales
Lista_Principal=None
VPaso=0
NoEmpresas=0
NOPunto=None
NOEmpresa=None
MinA=0
MaxA=0
PromA=0
Prom=0
Min=0
Max=0
Passs=0
TiempoEspera=0

#Limpiar consola
def refrescarPantalla():
    os.system("cls")
#Opción 1
def Limpiar_sistema():
    global Lista_Principal, VPaso,NoEmpresas
    Lista_Principal=None
    VPaso=0
    NoEmpresas=0
    input(Fore.LIGHTGREEN_EX+"Sistema Reseteado :)")
    refrescarPantalla()
#Opción 2
def lectura_XML_1():
    try:
        ventana=Tk()
        ventana.withdraw()
        ventana.attributes("-topmost",True)
        #Variables globales
        global VPaso, NoEmpresas, Lista_Principal
        
        ##Lectura del archivo con mensaje emergente
        ruta=filedialog.askopenfilename(title="Solo archivos xml")
        
        tree =ET.parse(ruta)
        root=tree.getroot() ## Obtiene la raíz

        if VPaso==0:
            #Inicializar lista
            Lista_Principal=ListaEmpresa()
            VPaso=1

        for i in range(0,len(root)):
            if Lista_Principal.comprobar(root[i].attrib["id"],NoEmpresas):
                Lista_Principal.agregarAListaUltimo(root[i].attrib["id"],root[i][0].text,root[i][1].text,str(len(root[i][2])),str(len(root[i][3]))) # IdEmpresa, Nombre, Abreviatura, CantPuntos,CantServicios
                NoEmpresas+=1
                print(Fore.LIGHTGREEN_EX+"Empresa "+str(NoEmpresas)+" cargada.")

                for j in range(0,len(root[i][2])):#cantidad de sucursales
                    Lista_Principal.agregarPunto(root[i][2][j].attrib["id"],root[i][2][j][0].text,root[i][2][j][1].text,str(len(root[i][2][j][2])),NoEmpresas)#IdPuntoA,Nombre,Direccion,CantEscritorios,NoEmpresa
                    for l in range(0,len(root[i][2][j][2])):
                        Lista_Principal.agregarEscritorio(root[i][2][j][2][l].attrib["id"],root[i][2][j][2][l][0].text,root[i][2][j][2][l][1].text,"Inactivo",NoEmpresas,j)#IdEscritorio,IdEncargado, NombreE, Estado,NoEmpresa,NoSucursal

                for k in range(0,len(root[i][3])):#cantidad de servicios
                    Lista_Principal.agregarServicio(root[i][3][k].attrib["id"],root[i][3][k][0].text,root[i][3][k][1].text,NoEmpresas)#IdServicio,NombreS,MinutosA,NoEmpresa
        
        input("")
        Lista_Principal.verInfoTotal(NoEmpresas)
        print(Fore.LIGHTGREEN_EX+"^ Datos cargados correctamente. ")
        input("")
    except IndexError:
        print(Fore.RED+"Ingrese un archivo de configuración válido.")
        Limpiar_sistema()
    except FileNotFoundError:
        print("")
#Opción 3
def CrearEmpresa():
    global NoEmpresas, Lista_Principal, VPaso
    NoSucursales=0
    Noservicios=0
    NoEscritorios=0
    salida=1

    if VPaso==0:
        #Inicializar lista
        Lista_Principal=ListaEmpresa()
        VPaso=1

    print("Información de Empresa ")
    print("Ingrese la siguiente información")
    idEmpresa=input("id: ")
    if Lista_Principal.comprobar(idEmpresa,NoEmpresas):
        NombreEmpresa=input("Nombre: ")
        Abreviatura=input("Abreviatura: ")
        Lista_Principal.agregarAListaUltimo(idEmpresa,NombreEmpresa,Abreviatura,str(0),str(0)) # IdEmpresa, Nombre, Abreviatura
        NoEmpresas+=1
        #print(Fore.LIGHTGREEN_EX+"Empresa "+str(NoEmpresas)+" cargada.")
        while salida==1:
            salida2=1
            NoEscritorios=0
            NoSucursales=NoSucursales+1
            print("---- Información de punto de atención ")
            print("---- Ingrese la siguiente información")
            idPunto=input("---- Identifiación: ")
            NombrePunto=input("---- Nombre: ")
            Direccion=input("---- Dirección: ")
            Lista_Principal.agregarPunto(idPunto,NombrePunto,Direccion,str(0),NoEmpresas)#IdPuntoA,Nombre,Direccion,NoEmpresa
            
            while salida2==1:
                NoEscritorios+=1
                print("--------- Información de escritorio ")
                print("--------- Ingrese la siguiente información")
                idEscritorio=input("--------- Id. Escritorio: ")
                IdentificaciónE=input("--------- Identificación: ")
                Encargado=input("--------- Encargado: ")

                Lista_Principal.agregarEscritorio(str(idEscritorio),str(IdentificaciónE),Encargado,"Inactivo",NoEmpresas,NoSucursales-1)#IdEscritorio,IdEncargado, NombreE, Estado,NoEmpresa,NoSucursal
                print("¿Añadir otro escritorio?")
                v=input("SI/NO: ")
                if v=="NO" or v=="No" or v=="no":
                    salida2=0 
            Lista_Principal.agregarCantEscritorioso(str(NoEscritorios),NoEmpresas,NoSucursales)
            
            print("¿Añadir otro punto de atención?")
            v=input("SI/NO: ")
            if v=="NO" or v=="No" or v=="no":
                salida=0 

        servicios=1
        while servicios==1:#cantidad de servicios
            Noservicios+=1
            print("---- Información de Servicios ")
            print("---- Ingrese la siguiente información")
            idTransición=input("---- Id. Transacción: ")
            NombreT=input("---- Nombre de transacción: ")
            Tiempo=input("---- Tiempo (min): ")
            Lista_Principal.agregarServicio(idTransición,NombreT,Tiempo,NoEmpresas)#IdServicio,NombreS,MinutosA,NoEmpresa
            print("¿Añadir otra transacción?")
            v=input("SI/NO: ")
            if v=="NO" or v=="No" or v=="no":
                servicios=0 

        Lista_Principal.agregarCantSerPun(str(NoSucursales),str(Noservicios),NoEmpresas)
#Opción 4
def lectura_XML_2():
    try:
        ventana=Tk()
        ventana.withdraw()
        ventana.attributes("-topmost",True)
        #Variables globales
        global VPaso, NoEmpresas, Lista_Principal


        if NoEmpresas>0:

            ##Lectura del archivo con mensaje emergente
            ruta=filedialog.askopenfilename(title="Solo archivos xml")
            tree =ET.parse(ruta)
            root=tree.getroot() ## Obtiene la raíz

            for i in range(0,len(root)): # Iterar cada configuración
                #print("Vuelta "+str(i))
                if Lista_Principal.PasoXML2(root[i].attrib["idEmpresa"],root[i].attrib["idPunto"],root[i].attrib["id"],NoEmpresas): # IdEmp,IdPunt,IdConfiguracion, NoEmpresas
                    #print("Paso "+str(i))
                    for j in range(0,len(root[i][0])):# Iterar escritorios
                        #print("intento:"+str(j))
                        Lista_Principal.CambiarEstado(root[i].attrib["idEmpresa"],root[i].attrib["idPunto"],NoEmpresas,root[i][0][j].attrib["idEscritorio"])#IdEmp,IdPunt,NoEmpresas,idEsc
                    #print("lista clientes: "+str(i))
                    for k in range(0,len(root[i][1])):# Iterar Clientes
                        tiempoTemp=0
                        for l in range(0,len(root[i][1][k][1])):# Iterar transacción
                            #print("transacción: "+str(l+1))
                            tiempoTemp=tiempoTemp+Lista_Principal.ObtenerTiempo(NoEmpresas,root[i].attrib["idEmpresa"],root[i][1][k][1][l].attrib["idTransaccion"],int(root[i][1][k][1][l].attrib["cantidad"]))#NoEmpresas,IDempresa,IDServicio,Cant
                        Lista_Principal.agregarCliente(root[i][1][k].attrib["dpi"],root[i][1][k][0].text,str(tiempoTemp),NoEmpresas,root[i].attrib["idEmpresa"],root[i].attrib["idPunto"])#DPI,NombreC,tiempoAtencion,NoEmpresa,IDempresa,IDsucursal
                        #print(Fore.LIGHTGREEN_EX+"cliente "+str(k+1)+" cargado.")
                    #input("listo")
                    print("")
                    print("")
                    print("")
                    Lista_Principal.verInfoTotalTotal(NoEmpresas,root[i].attrib["idEmpresa"],root[i].attrib["idPunto"])#NoEmpresa,ID,IDsucursal
            #print("Listo x2")
            print("")
            print(Fore.LIGHTGREEN_EX+"^ Datos cargados correctamente. ")
            input("")
        else:
            input(Fore.RED+"Cargue primero el archivo de configuración inicial. B(")

    except IndexError:
        print(Fore.RED+"Ingrese un archivo de configuración válido.")
        Limpiar_sistema()
    #except syntax error:
        #print("asfkjasdfklaj")
    except FileNotFoundError:
        print("")

def MostrarMenú2():
    Operación=0
    salida=0
    global Lista_Principal,NoEmpresas
    global NOEmpresa,NOPunto, Passs
    if NoEmpresas>0:
        while salida==0:
            refrescarPantalla()
            # Menú empresas
            Lista_Principal.mostrarMenu2(NoEmpresas)
            
            print(Fore.LIGHTCYAN_EX+"Ingrese el número de empresa: ",end="")
            
            Operación = input(Fore.LIGHTWHITE_EX+"")
            
            try:
                # Si la opción es incorrecta 
                if int(Operación)<1 or int(Operación)>NoEmpresas+1:
                    input(Fore.RED+"Ingrese una opción válida.")
                # Si la opción es correcta
                else:
                    # Válidar salida
                    if int(Operación)==(NoEmpresas+1):
                        salida=1
                        refrescarPantalla()
                    # Guardar id empresa
                    else:
                        OBEmpresa=Lista_Principal.IterarEmpresas(int(Operación))
                        

                        #print(NOEmpresa)
                        #Lista_Principal.IterarEmpresas(int(Operación))
                        OBPunto=Lista_Principal.MostrarSucursal(int(Operación))
                        #print(NOPunto)
                        #input("")
                        salida=1

                        Passs=0
                        return OBEmpresa,OBPunto                        
            except ValueError:
                input(Fore.RED+"Ingrese un valor numérico.")
                refrescarPantalla()
    else:
        refrescarPantalla()
        print(Fore.RED+"No hay empresas cargadas. D: ")
        return None, None




def VerEstadoAtencion(Empresa,Punto):
    print("")
    print(Fore.LIGHTBLUE_EX+"    .-.-.-.-.- INFORMACION GENERADA -.-.-.-.-.")
    print("     ")

    print(Fore.LIGHTCYAN_EX+"Empresa "+Fore.LIGHTWHITE_EX+str(Empresa.Nombre))
    print(Fore.LIGHTCYAN_EX+"Punto de atención "+Fore.LIGHTWHITE_EX+str(Punto.Nombre)+":")
    print(Fore.LIGHTCYAN_EX+"       Cantidad de escritorios activos: "+Fore.LIGHTWHITE_EX+str(Punto.CantEscrActivados))
    print(Fore.LIGHTCYAN_EX+"       Cantidad de escritorios inactivos: "+Fore.LIGHTWHITE_EX+str(Punto.CantEscrInactivos))
    print(Fore.LIGHTCYAN_EX+"       Clientes por atender: "+Fore.LIGHTWHITE_EX+str(Punto.CantClientes-1))
    print(Fore.LIGHTCYAN_EX+"       Tiempo promedio de espera: "+Fore.LIGHTWHITE_EX+str(Punto.TiempoPromedioEspera))
    print(Fore.LIGHTCYAN_EX+"       Tiempo mínimo de espera: "+Fore.LIGHTWHITE_EX+str(Punto.TiempoMinEspera))
    print(Fore.LIGHTCYAN_EX+"       Tiempo máximo de espera: "+Fore.LIGHTWHITE_EX+str(Punto.TiempoMaxEspera))
    print(Fore.LIGHTCYAN_EX+"       Tiempo promedio de atención: "+Fore.LIGHTWHITE_EX+str(Punto.TiempoPromAtencion))
    print(Fore.LIGHTCYAN_EX+"       Tiempo mínimo de atención: "+Fore.LIGHTWHITE_EX+str(Punto.TiempoMinAtencion))
    print(Fore.LIGHTCYAN_EX+"       Tiempo máximo de atención: "+Fore.LIGHTWHITE_EX+str(Punto.TiempoMaxAtencion))
    print("")
    print(Fore.LIGHTBLUE_EX+" ----------------- Escritorios -----------------")
    Escritorios=Punto.PrimerEscritorio
    j=1
    print("")
    for i in range(0,int(Punto.CantEscritorios)):
        if Escritorios.Estado=="Activo":
            print(Fore.LIGHTCYAN_EX+"   Escritorio "+str(j)+": ")
            print(Fore.LIGHTCYAN_EX+"       ID Escritorio: "+Fore.LIGHTWHITE_EX+str(Escritorios.IdEscritorio))
            print(Fore.LIGHTCYAN_EX+"       Tiempo promedio de atención: "+Fore.LIGHTWHITE_EX+str(Escritorios.TiempoPromAntecion))
            print(Fore.LIGHTCYAN_EX+"       Tiempo promedio de atención: "+Fore.LIGHTWHITE_EX+str(Escritorios.TiempoPromAntecion))
            print(Fore.LIGHTCYAN_EX+"       Tiempo mínimo de atención: "+Fore.LIGHTWHITE_EX+str(Escritorios.TiempoMinAtencion))
            print(Fore.LIGHTCYAN_EX+"       Tiempo máximo de atención: "+Fore.LIGHTWHITE_EX+str(Escritorios.TiempoMaxAtencion))
            print("")
            j+=1
        Escritorios=Escritorios.ESIG
    
def CambiarEstadoInactivo(Empresa,Punto):
    refrescarPantalla()
    j=1
    try:
        if Punto.CantEscrInactivos=="0":
            input("No se encuentran escritorios desactivados. B)")
        else:
            Escritorios=Punto.PrimerEscritorio
            print()
            print(    "No. | Código")
            print(    "---------------------------------")
            for i in range(0,int(Punto.CantEscritorios)):
                if Escritorios.Estado=="Inactivo":
                    print("  "+str(j)+".  "+Escritorios.IdEscritorio)
                    Escritorios=Escritorios.ESIG
                    j+=1
                else:
                    Escritorios=Escritorios.ESIG
            print(    "---------------------------------")
            v=input("Escoja el escritorio: ")
            
            Escritorios2=Punto.PrimerEscritorio
            v2=0
            if int(v)>=0 and int(v)<int(Punto.CantEscrInactivos)+1:
                while v2!=int(v):
                    if Escritorios2.Estado=="Inactivo":
                        v2+=1
                    if v2!=int(v):
                        Escritorios2=Escritorios2.ESIG

                Escritorios2.Estado="Activo"
                Punto.CantEscrActivados=int(Punto.CantEscrActivados)+1
                Punto.CantEscrInactivos=int(Punto.CantEscrInactivos)-1
                print(Punto.CantEscrActivados)
                print(Punto.CantEscrInactivos)
    
    except ValueError:
        print("Escoja un escritorio válido.")
    except TypeError:
        print("")

def CambiarEstadoActivo(Empresa,Punto):
    refrescarPantalla()
    j=1
    try:
        if Punto.CantEscrActivados=="0":
            input("No se encuentran escritorios activados. B)")
        else:
            Escritorios=Punto.PrimerEscritorio
            print()
            print(    "No. | Código")
            print(    "---------------------------------")
            for i in range(0,int(Punto.CantEscritorios)):
                if Escritorios.Estado=="Activo":
                    print("  "+str(j)+".  "+Escritorios.IdEscritorio)
                    Escritorios=Escritorios.ESIG
                    j+=1
                else:
                    Escritorios=Escritorios.ESIG
            print(    "---------------------------------")
            v=input("Escoja el escritorio: ")
            
            Escritorios2=Punto.PrimerEscritorio
            v2=0
            if int(v)>0 and int(v)<int(Punto.CantEscrActivados)+1:
                while v2!=int(v):
                    if Escritorios2.Estado=="Activo":
                        v2+=1
                    if v2!=int(v):
                        Escritorios2=Escritorios2.ESIG
                Escritorios2.Estado="Inactivo"
                Punto.CantEscrActivados=str(int(Punto.CantEscrActivados)-1)
                Punto.CantEscrInactivos=str(int(Punto.CantEscrInactivos)+1)
                print(Punto.CantEscrActivados)
                print(Punto.CantEscrInactivos)
    
    except ValueError:
        print("Escoja un escritorio válido.")
    except TypeError:
        print("")

def AtenderCliente(Empresa,Punto):
    #refrescarPantalla()
    salir=1
    tiempo=0
    try:
        DPI=input(Fore.LIGHTWHITE_EX+"Ingrese el DPI del cliente: "+Fore.LIGHTCYAN_EX)
        Nombre=input(Fore.LIGHTWHITE_EX+"Ingrese el Nombre: "+Fore.LIGHTCYAN_EX)
        
        while salir==1:
            temp=Empresa.PrimerServicio
            print(Fore.LIGHTWHITE_EX+"______________________________________________")
            print("Servicios:")
            for i in range(0,int(Empresa.CantServicios)):
                print(str(i+1)+". "+temp.NombreS)
                temp=temp.SIG
            #print("______________________________________________")
            print("----------------------------------------------")
            v=input("Ingrese el número de servicio servicio: "+Fore.LIGHTCYAN_EX)
            v2=1
            temp2=Empresa.PrimerServicio
            if int(v)>0 and int(v)<int(Empresa.CantServicios)+1:
                while v2!=int(v):
                    v2+=1
                    temp2=temp2.SIG
                tiempo=tiempo+int(temp2.MinutosA)
                print("¿Quiere realizar otra transacción? ")
                a=input("SI/NO ")
                if a=="NO" or a=="No" or a=="no" or a=="nO":
                    salir=0
        Punto.agregarAListaUltimoCliente(DPI,Nombre,tiempo)
        Punto.CantClientes=int(Punto.CantClientes)+1
        Punto.CantClientes2=int(Punto.CantClientes2)+1
        
        Punto.recorrerInicio_FinCliente(int(Punto.CantClientes))

        input(Fore.LIGHTGREEN_EX+"Ingresado correctamente.")
        print("")
        
    except ValueError:
        print("Escoja un servicio válido válido.")
    except TypeError:
        print("dddddd")

def LlenarEscritorios(Empresa,Punto):
    temp=Punto.PrimerEscritorio
    
    Clientes=0
    
    global Passs,TiempoEspera
    if Punto.CantClientes>1:
        print(Fore.LIGHTCYAN_EX+"   -----------------------------")
        for i in range(0,int(Punto.CantEscritorios)):
            Cliente=Punto.PrimerCliente
            if temp.Disponible=="SI" and temp.Estado=="Activo" and Punto.CantClientes>1:
                
                temp.TiempoActual=int(Cliente.tiempoAtencion)
                TiempoEspera=TiempoEspera+temp.TiempoActual
                Punto.TiempoTotal=Punto.TiempoTotal+int(temp.TiempoActual)
                Punto.CantAtendiendo=Punto.CantAtendiendo+1
                #print(str(Punto.TiempoTotal))
                Punto.TiempoPromedioEspera=int(TiempoEspera)/int(Punto.CantEscrActivados)
                Punto.TiempoPromAtencion=Punto.TiempoTotal/Punto.CantAtendiendo
                    #Tiempo Atención
                if temp.TiempoActual>Punto.TiempoMaxAtencion:
                    Punto.TiempoMaxAtencion=temp.TiempoActual
                if temp.TiempoActual<Punto.TiempoMinAtencion:
                    Punto.TiempoMinAtencion=temp.TiempoActual
                    #Tiempo de Espera
                if temp.TiempoActual<Punto.TiempoMinEspera:
                    Punto.TiempoMinEspera=temp.TiempoActual
                if temp.TiempoActual>Punto.TiempoMaxEspera:
                    Punto.TiempoMaxEspera=temp.TiempoActual

                temp.NumClientes=temp.NumClientes+1
                temp.TiempoTotal=temp.TiempoTotal+temp.TiempoActual
                temp.TiempoPromAntecion=temp.TiempoTotal/temp.NumClientes
                temp.ClienteNom=Cliente.NombreC
                if temp.TiempoActual<temp.TiempoMinAtencion:
                    temp.TiempoMinAtencion= temp.TiempoActual
                if temp.TiempoActual>temp.TiempoMaxAtencion:
                    temp.TiempoMaxAtencion=temp.TiempoActual
                
                input(Fore.LIGHTCYAN_EX+"   Se está atendiendo a: "+Fore.LIGHTWHITE_EX+Cliente.NombreC)
                Punto.eliminar_inicioCliente()
                Punto.CantClientes=int(Punto.CantClientes)-1
                #print(Punto.CantClientes)
                temp.Disponible="NO"
                #Punto.recorrerInicio_FinCliente(int(Punto.CantClientes))
            temp=temp.ESIG

def retirarCliente(Empresa,Punto):
    global TiempoEspera
    TiempoEspera=0
    TiempoTemp=1000000000000
    Vmin=100000000
    VMax=0
    if int(Punto.CantEscrActivados)==0:
        input("No se encuentran escritorios activados.")
        refrescarPantalla()
    elif int(Punto.CantClientes2)==1:
        input("No quedan más clientes por atender.")
        refrescarPantalla()
    else:
        Escritorios=Punto.PrimerEscritorio
        #BuscarTiempoMinimo
        for i in range(0,int(Punto.CantEscritorios)):
            if Escritorios.Disponible=="NO":
                if int(Escritorios.TiempoActual)<TiempoTemp:
                    TiempoTemp=int(Escritorios.TiempoActual)
            Escritorios=Escritorios.ESIG
        #print("tiempo minimo: "+str(TiempoTemp))
        #RestarTiempoTodos
        Escritorios=Punto.PrimerEscritorio
        for i in range(0,int(Punto.CantEscritorios)):
            if Escritorios.Disponible=="NO":
                Escritorios.TiempoActual=int(Escritorios.TiempoActual)-TiempoTemp
                #print("hola")
            Escritorios=Escritorios.ESIG
        
        #BuscarTiempos <=0
            #- Retirar Cliente Escritorio
            #- Disponibilidad="SI"
        Escritorios=Punto.PrimerEscritorio
        for i in range(0,int(Punto.CantEscritorios)):
            if Escritorios.Disponible=="NO":
                if Escritorios.TiempoActual==0:
                    print(Fore.LIGHTBLUE_EX+"       Cliente atendido felizmente: "+Fore.LIGHTGREEN_EX+Escritorios.ClienteNom)
                    
                    Escritorios.Disponible="SI"
                    Escritorios.ClienteNom=None
                    Escritorios.TiempoActual=0
                    Punto.CantClientes2=Punto.CantClientes2-1
                    #print(str(Punto.CantClientes2))
            Escritorios=Escritorios.ESIG
        
        Escritorios=Punto.PrimerEscritorio
        for i in range(0,int(Punto.CantEscritorios)):
            if Escritorios.Disponible=="NO":
                TiempoEspera=TiempoEspera+int(Escritorios.TiempoActual)
                if Escritorios.TiempoActual<Vmin:
                    Vmin=Escritorios.TiempoActual
                if Escritorios.TiempoActual>VMax:
                    VMax=Escritorios.TiempoActual
            Escritorios=Escritorios.ESIG

        if Punto.CantClientes2==1:
            print(Fore.LIGHTCYAN_EX+"-----------------------------")
            input(Fore.LIGHTGREEN_EX+"En espera de más clientes. :)")
            refrescarPantalla()
            return False
        elif Punto.CantClientes==1:
            return True
        else:

            Punto.TiempoMinEspera=Vmin
            Punto.TiempoMaxEspera=VMax
            #LlenarEscritorios
            LlenarEscritorios(Empresa,Punto)
            print(Fore.LIGHTCYAN_EX+"   -----------------------------")
            return True

def simularAtención(Empresa,Punto):
    Salida=True
    
    print(Fore.LIGHTWHITE_EX+"         .-.-.-.-.- SIMULACION -.-.-.-.-.")
    print("     ")

    while Salida:
        Salida=retirarCliente(Empresa,Punto)

    print("SIMULACION TERMINADA---------------------------")
    VerEstadoAtencion(Empresa,Punto)
    grafica2(Empresa,Punto)


def GraphizInfo(Empresa,Punto):
    Escritorios=Punto.PrimerEscritorio
    text=None
    text=""
    text+="node [shape=rect border=\"1\" cellspacing=\"1\" cellpadding=\"1\" style=\"rounded\"  ];\n"    
    text+="node [fontname=\"Helvetica,Arial,sans-serif\" color=\"#28646D\"];\n"    
    text+="edge [fontname=\"Helvetica,Arial,sans-serif\" color=\"#28646D\"];\n"
    text+="OrdenACTIVOS [label=<<TABLE border=\"1\" cellspacing=\"8\" cellpadding=\"8\" style=\"rounded\" bgcolor=\"#28646D\" >\n"
    text+=" <TR>\n"
    text+="     <TD bgcolor=\"#B8ECF4\" >ACTIVOS</TD>\n"
    text+=" </TR>\n"
    text+=" </TABLE>>];"

    text+="OrdenINACTIVOS [label=<<TABLE border=\"1\" cellspacing=\"8\" cellpadding=\"8\" style=\"rounded\" bgcolor=\"#28646D\" >\n"
    text+=" <TR>\n"
    text+="     <TD bgcolor=\"#B8ECF4\" >INACTIVOS</TD>\n"
    text+=" </TR>\n"
    text+=" </TABLE>>];"

    text+="OrdenESCRITORIOS [label=<<TABLE border=\"1\" cellspacing=\"8\" cellpadding=\"8\" style=\"rounded\" bgcolor=\"#28646D\" >\n"
    text+=" <TR>\n"
    text+="     <TD bgcolor=\"#B8ECF4\" >ESCRITORIOS</TD>\n"
    text+=" </TR>\n"
    text+=" </TABLE>>];"

    for i in range(0,int(Punto.CantEscritorios)):
        text+="Orden"+str(i)+" [label=<<TABLE border=\"1\" cellspacing=\"8\" cellpadding=\"8\" style=\"rounded\" bgcolor=\"#28646D\" >\n"
        
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" colspan=\"2\">"+"ID: "+Escritorios.IdEscritorio+"</TD>\n"
        text+=" </TR>\n"
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >Clientes atendidos</TD>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >"+str(Escritorios.NumClientes)+"</TD>\n"
        text+=" </TR>\n"
        if Escritorios.ClienteNom==None:
            v="Limpio"
        else:
            v=Escritorios.ClienteNom
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >Cliente atendiendo</TD>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >"+str(v)+"</TD>\n"
        text+=" </TR>\n"
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >Tiempo promedio</TD>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >"+str(Escritorios.TiempoPromAntecion)+" min</TD>\n"
        text+=" </TR>\n"
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >Tiempo minimo</TD>\n"
        if Escritorios.TiempoMinAtencion==10000000:
            Escritorios.TiempoMinAtencion=0
        text+="     <TD bgcolor=\"#B8ECF4\" >"+str(Escritorios.TiempoMinAtencion)+" min</TD>\n"
        text+=" </TR>\n"
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\">Tiempo maximo</TD>\n"
        text+="     <TD bgcolor=\"#B8ECF4\">"+str(Escritorios.TiempoMaxAtencion)+" min</TD>\n"
        text+=" </TR>\n"
        text+=" </TABLE>>];"
        Escritorios=Escritorios.ESIG
    
    Clientes=Punto.UltimoCliente
    Valor=int(Punto.CantClientes)-1
    for i in range(0,int(Punto.CantClientes)-1):
        text+="Orden"+str(i+10)+" [label=<<TABLE border=\"1\" cellspacing=\"8\" cellpadding=\"8\" style=\"rounded\" bgcolor=\"#28646D\" >\n"
        
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" colspan=\"2\">"+"Cliente "+str(Valor-i)+"</TD>\n"
        text+=" </TR>\n"
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >DPI</TD>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >"+str(Clientes.DPI)+"</TD>\n"
        text+=" </TR>\n"
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >Nombre</TD>\n"
        text+="     <TD bgcolor=\"#B8ECF4\" >"+str(Clientes.NombreC)+"</TD>\n"
        text+=" </TR>\n"
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\">Tiempo de atencion</TD>\n"
        text+="     <TD bgcolor=\"#B8ECF4\">"+str(Clientes.tiempoAtencion)+" min</TD>\n"
        text+=" </TR>\n"
        text+=" </TABLE>>];"
        Clientes=Clientes.Cant


    Escritorios=Punto.PrimerEscritorio
    for i in range(0,int(Punto.CantEscritorios)):
        if i==0:
            text+="\n"
            text+="OrdenESCRITORIOS->OrdenACTIVOS\n"
            text+="OrdenESCRITORIOS->OrdenINACTIVOS\n"
            text+="\n"
            Activo="ACTIVOS"
            Inactivo="INACTIVOS"

        if  Escritorios.Estado=="Activo":
            text+="\n"
            text+="Orden"+Activo+"->Orden"+str(i)+"\n"
            text+="\n"
            Activo=str(i)
        
        if  Escritorios.Estado=="Inactivo":
            text+="\n"
            text+="Orden"+Inactivo+"->Orden"+str(i)+"\n"
            text+="\n"
            Inactivo=str(i)
        Escritorios=Escritorios.ESIG

    if Punto.CantClientes==1:
        text+="Orden10"+" [label=<<TABLE border=\"1\" cellspacing=\"8\" cellpadding=\"8\" style=\"rounded\" bgcolor=\"#28646D\" >\n"
        
        text+=" <TR>\n"
        text+="     <TD bgcolor=\"#B8ECF4\">"+"Sin clientes en cola </TD>\n"
        text+=" </TR>\n"
        
        text+=" </TABLE>>];"

        text+="CLIENTES_EN_ESPERA->Orden10"

    for i in range(0,int(Punto.CantClientes)-1):
        if i==0:
            text+="\n"
            text+="CLIENTES_EN_ESPERA->Orden"+str(i+10)+"\n"
            text+="\n"
        text+="\n"
        text+="Orden"+str(i+10)+"->Orden"+str(i+11)+"\n"
        text+="\n"

    return text

def grafica(Empresa,Punto):
    
    contenido="digraph G{\n\n"
    r=open("grafica.txt","w")
    contenido+=GraphizInfo(Empresa,Punto)
    contenido+="\n}"
    r.write(contenido)
    r.close()
    print("Gráfica generada")
    os.system("dot -Tpng grafica.txt -o Grafica"+".png") 

def grafica2(Empresa,Punto):
    
    contenido="digraph G{\n\n"
    r=open("grafica.txt","w")
    contenido+=GraphizInfo(Empresa,Punto)
    contenido+="\n}"
    r.write(contenido)
    r.close()
    print("Gráfica generada")
    os.system("dot -Tpng grafica.txt -o Grafica_SIMULACION"+".png") 