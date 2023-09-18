from asyncio.windows_events import NULL
from colorama import Fore
import os


#1 Lista Empresas
class ListaEmpresa():
    #Lista Empresa: Incializar lista
    def __init__(self):
        self.Primero=None
        self.Ultimo=None
    
    #Lista Empresa: Comprobar si está vacía
    def estaVacia(self):
        if self.Primero==None:
            return True
        else:
            return False 
    
    #Lista Empresa: Añade la empresa al final
    def agregarAListaUltimo(self,IdEmpresa, Nombre, Abreviatura, CantPuntos, CantServicios):
        nuevo= Empresa(IdEmpresa, Nombre, Abreviatura, CantPuntos,CantServicios)
        if self.estaVacia():
            self.Primero=self.Ultimo=nuevo
        else:
            temp=self.Ultimo
            self.Ultimo=temp.SIGUIENTE=nuevo
            self.Ultimo.ANTERIOR=temp
        self.NullearNodos()
    
    #Lista Empresa: orientar límites de los apuntadores
    def NullearNodos(self):
        if self.Primero!=None:
            self.Primero.ANTERIOR=NULL
            self.Ultimo.SIGUIENTE=NULL
    
    #Lista Empresa: Imprimir solo los datos de empresa
    def recorrerInicio_Fin(self,NoEmpresas):
        temp0=self.Primero
    
        for i in range(0,NoEmpresas):
            print(Fore.BLUE+"id: "+temp0.IdEmpresa)
            print(Fore.BLUE+"Nombre: "+temp0.Nombre)
            print(Fore.BLUE+"Abreviatura: "+temp0.Abreviatura)
            print(Fore.BLUE+"No. Sucursales: "+temp0.CantPuntos)
            print(Fore.BLUE+"No. Servicios: "+temp0.CantServicios)
            print("")
            temp0=temp0.SIGUIENTE
    
    #Lista Empresa: Imprimir solo los puntos de atención
    def verInfoPuntos(self,No): 
        temp=self.Primero
        for i in range(0,No):
            temp=temp.SIGUIENTE
        temp.recorrerInicio_FinE(temp.CantPuntos) 
        
    #Lista Empresa: Comprobar que exista la empresa
    def comprobar(self, Comprobación, NoEmpresas):
        temp0=self.Primero
        for i in range(0,NoEmpresas):
            if temp0.IdEmpresa==Comprobación:
                print(Fore.RED+"Empresa repetida: "+temp0.Nombre)
                return False
            temp0=temp0.SIGUIENTE
        return True

    #Lista Empresa: Abre paso para que se guarde la configuración
    def PasoXML2(self, IdEmp,IdPunt,IdConfiguracion, NoEmpresas):
        temp0=self.Primero
        salida=1
        v=0
        for i in range(0,NoEmpresas):
            if temp0.IdEmpresa==IdEmp:
                v=1
                break
            temp0=temp0.SIGUIENTE
        
        if v==1:
            temp1=temp0.PrimerPuntoA
            while salida==1:
                #print("hola")
                if temp1.IdPuntoA==IdPunt:
                    salida=0
                    #print("adiós")
                    break
                if temp1.CONTINUAR==NULL:
                    salida=0
                    print(Fore.RED+"No se encontro la sucursal con el id: "+IdPunt)
                    return False
                temp1=temp1.CONTINUAR
            temp1.IdConfig=IdConfiguracion
            #print (Fore.GREEN+"Verifiaciones de id's hecha.")
            return True
        else:
            print(Fore.RED+"No se encontro la empresa con id: "+IdEmp)
            return False
        
    #Lista Empresa: Cambia el estado de los escritorios por su código
    def CambiarEstado(self,IdEmp,IdPunt,NoEmpresas,idEsc):
        temp0=self.Primero
        salida=1
        for i in range(0,NoEmpresas):
            if temp0.IdEmpresa==IdEmp:
                break
            temp0=temp0.SIGUIENTE
        temp1=temp0.PrimerPuntoA
        while salida==1:
            if temp1.IdPuntoA==IdPunt:
                salida=0
                break
            temp1=temp1.CONTINUAR
        temp2=temp1.PrimerEscritorio
        salida3=0
        while salida3==0:
            if temp2.IdEscritorio==idEsc:
                temp2.Estado="Activo"
                temp1.CantEscrInactivos=int(temp1.CantEscrInactivos)-1
                temp1.CantEscrActivados=temp1.CantEscrActivados+1
                salida3=1
                break
            if temp2==NULL:
                salida3=1
                print(Fore.RED+"    No se encontro el escritorio con el id: "+idEsc)
                break
            temp2=temp2.ESIG

    #----------------------- AGREGAR INFORMACION -------------------------------------
    #Lista Empresa: Agrega un nuevo cliente a un punto de atención
    def agregarCliente(self,DPI,NombreC,tiempoAtencion,NoEmpresa,IDempresa,IDsucursal):
        temp0=self.Primero
        salida=1
        for i in range(0,NoEmpresa):
            if temp0.IdEmpresa==IDempresa:
                break
            temp0=temp0.SIGUIENTE
        temp1=temp0.PrimerPuntoA
        while salida==1:
            if temp1.IdPuntoA==IDsucursal:
                salida=0
                break
            temp1=temp1.CONTINUAR
        temp1.agregarAListaUltimoCliente(DPI,NombreC,tiempoAtencion)
        temp1.CantClientes=int(temp1.CantClientes+1)
        
    #Lista Empresa: Obtener tiempo de clientes
    def ObtenerTiempo(self,NoEmpresas,IDempresa,IDServicio,Cant):
        temp0=self.Primero
        salida=1
        for i in range(0,NoEmpresas):
            if temp0.IdEmpresa==IDempresa:
                break
            temp0=temp0.SIGUIENTE
        temp1=temp0.PrimerServicio
        while salida==1:
            if temp1.IdServicio==IDServicio:
                salida=0
                break
            if temp1==NULL:
                salida=0
                print(Fore.RED+"    No se encontro el servicio con el id: "+IDServicio)
                return 0
            temp1=temp1.SIG
        tiempoAtención= int(temp1.MinutosA)*Cant
        return int(tiempoAtención)

    #Lista Empresa: Agrega un punto de atención
    def agregarPunto(self,IdPuntoA,Nombre,Direccion,CantEscritorios,NoEmpresa):
        temp0=self.Primero
        for i in range(0,NoEmpresa-1):
            temp0=temp0.SIGUIENTE
        temp0.agregarAListaUltimoE(IdPuntoA,Nombre,Direccion,CantEscritorios)
        
    #Lista Empresa: Agrega la cantidad de escritorios
    def agregarCantEscritorioso(self,CantEscritorios,NoEmpresa,Nosucursal):
        temp0=self.Primero
        for i in range(0,NoEmpresa-1):
            temp0=temp0.SIGUIENTE
        temp=temp0.PrimerPuntoA
        for j in range(0,Nosucursal-1):
            temp=temp.CONTINUAR
        temp.CantEscritorios=CantEscritorios

    #Lista Empresa: Agrega la cantidad de Servicios y Puntos
    def agregarCantSerPun(self,Punto,servicios,NoEmpresa):
        temp0=self.Primero
        for i in range(0,NoEmpresa-1):
            temp0=temp0.SIGUIENTE
        temp0.CantPuntos=Punto
        temp0.CantServicios=servicios
    
    #Lista Empresa: Agrega un Escritorio
    def agregarEscritorio(self,IdEscritorio,IdEncargado, NombreE, Estado,NoEmpresa,NoSucursal):
        temp0=self.Primero
        for i in range(0,NoEmpresa-1):
            temp0=temp0.SIGUIENTE
        temp=temp0.PrimerPuntoA
        for j in range(0,NoSucursal):
            temp=temp.CONTINUAR
        temp.agregarAListaUltimoEscritorio(IdEscritorio,IdEncargado, NombreE, Estado)
        temp.CantEscrInactivos=int(temp.CantEscritorios)

    #Lista Empresa: Agrega un servicio
    def agregarServicio(self,IdServicio,NombreS,MinutosA,NoEmpresa):
        temp0=self.Primero
        for i in range(0,NoEmpresa-1):
            temp0=temp0.SIGUIENTE
        temp0.agregarAListaUltimoServicio(IdServicio,NombreS,MinutosA)
    
    #---------------------- Imprimir información ----------------------
    #Lista Empresa: Ver toda la información de una empresa
    def verInfoEspecifico(self,idEmpresa,NoEmpresa): 
        temp=self.Primero
        v=0
        for i in range(0,NoEmpresa):
            if temp.IdEmpresa==idEmpresa:
                v=1
                break
            temp=temp.SIGUIENTE

        if v==1:
          temp.recorrerInicio_FinE(temp.CantPuntos)
          temp.recorrerInicio_FinServicio(temp.CantServicios)  
        else:
            print("No existe dicho código")
    
    #Lista Empresa: Ver toda la información
    def verInfoTotal(self,NoEmpresa): 
        temp=self.Primero
        print("")
        v=0
        for i in range(0,NoEmpresa):
            
            print(Fore.LIGHTBLUE_EX+"---------------------------- "+str(i+1)+" ------------------------------")
            print(Fore.LIGHTWHITE_EX+"                          EMPRESA                          ")
            print(Fore.LIGHTWHITE_EX+"  id: "+Fore.LIGHTCYAN_EX+temp.IdEmpresa)
            print(Fore.LIGHTWHITE_EX+"  Nombre: "+Fore.LIGHTCYAN_EX+temp.Nombre)
            print(Fore.LIGHTWHITE_EX+"  Abreviatura: "+Fore.LIGHTCYAN_EX+temp.Abreviatura)
            print(Fore.LIGHTWHITE_EX+"  No. Sucursales: "+Fore.LIGHTCYAN_EX+temp.CantPuntos)
            print(Fore.LIGHTWHITE_EX+"  No. Servicios: "+Fore.LIGHTCYAN_EX+temp.CantServicios)
            print("")
            print(Fore.LIGHTCYAN_EX+"        ------------"+Fore.LIGHTWHITE_EX+" PUNTOS DE ATENCIÓN "+Fore.LIGHTCYAN_EX+"------------         ")
            print("")
            temp.recorrerInicio_FinE(temp.CantPuntos)
            print(Fore.LIGHTCYAN_EX+"        -----------------"+Fore.LIGHTWHITE_EX+" SERVICIOS "+Fore.LIGHTCYAN_EX+"-----------------        ")
            print("")
            temp.recorrerInicio_FinServicio(temp.CantServicios) 
            temp=temp.SIGUIENTE              
    
    #Lista Empresa: Ver toda la información de configuración            
    def verInfoTotalTotal(self,NoEmpresa,ID,IDsucursal): 
        temp=self.Primero
        v=0
        u=0
        for i in range(0,NoEmpresa):
            if temp.IdEmpresa==ID:
                
                print(Fore.LIGHTBLUE_EX+"--------------------- CONFIGURACIÓN "+IDsucursal+" ------------------------")
                print(Fore.LIGHTWHITE_EX+"                          EMPRESA                          ")
                print(Fore.LIGHTWHITE_EX+"  id: "+Fore.LIGHTCYAN_EX+temp.IdEmpresa)
                print(Fore.LIGHTWHITE_EX+"  Nombre: "+Fore.LIGHTCYAN_EX+temp.Nombre)
                print(Fore.LIGHTWHITE_EX+"  Abreviatura: "+Fore.LIGHTCYAN_EX+temp.Abreviatura)
                print(Fore.LIGHTWHITE_EX+"  No. Sucursales: "+Fore.LIGHTCYAN_EX+temp.CantPuntos)
                print(Fore.LIGHTWHITE_EX+"  No. Servicios: "+Fore.LIGHTCYAN_EX+temp.CantServicios)
                print("")
                print(Fore.LIGHTCYAN_EX+"        ------------"+Fore.LIGHTWHITE_EX+" PUNTOS DE ATENCIÓN "+Fore.LIGHTCYAN_EX+"------------         ")
                print("")
                temp.recorrerInicio_FinE2(temp.CantPuntos,IDsucursal)
                #print(Fore.LIGHTCYAN_EX+"        -----------------"+Fore.LIGHTWHITE_EX+" SERVICIOS "+Fore.LIGHTCYAN_EX+"-----------------        ")
                #print("")
                #temp.recorrerInicio_FinServicio(temp.CantServicios) 
                u=u+1
            temp=temp.SIGUIENTE

    #----------------------- SUB MENU 2 -------------------------------------
    def mostrarMenu2(self,NoEmpresas):
        empresas=self.Primero
        print("")
        print(Fore.LIGHTBLUE_EX+" .-.-.-. "+"\""+Fore.LIGHTCYAN_EX+"Soluciones Guatemaltecas, S.A."+Fore.LIGHTBLUE_EX+"\""+              " .-.-.-. ")
        print("")
        print(Fore.LIGHTBLUE_EX+"   "+Fore.LIGHTBLUE_EX+"LISTADO DE EMPRESAS:                    ")
        print("")
        for i in range(0,NoEmpresas):
            print(Fore.LIGHTBLUE_EX+"   "+Fore.LIGHTWHITE_EX+str(i+1)+Fore.LIGHTCYAN_EX+" "+empresas.Nombre)
            empresas=empresas.SIGUIENTE
        print(Fore.LIGHTBLUE_EX+"   "+Fore.LIGHTWHITE_EX+str(i+2)+Fore.LIGHTCYAN_EX+" Regresar")
        print("")
        print(Fore.LIGHTBLUE_EX+" -.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.- ")

    def IterarEmpresas(self,Operación):
        Buscar=self.Primero
        for i in range(0,Operación-1):
            Buscar=Buscar.SIGUIENTE
        return Buscar #.IdEmpresa,Buscar.Nombre
        
    def MostrarSucursal(self,Operación):
        def refrescarPantalla():
            os.system("cls")    
        
        salida=0
        
        while salida==0:
            empresas=self.Primero
            for i in range(0,Operación-1):
                empresas=empresas.SIGUIENTE
            PuntoAtención=empresas.PrimerPuntoA
            refrescarPantalla()
            print("")
            print(Fore.LIGHTBLUE_EX+" .-.-.-. "+"\""+Fore.LIGHTCYAN_EX+"Soluciones Guatemaltecas, S.A."+Fore.LIGHTBLUE_EX+"\""+              " .-.-.-. ")
            print("")
            print(Fore.LIGHTBLUE_EX+"   "+Fore.LIGHTBLUE_EX+"PUNTOS DE ATENCIÓN:                    ")
            print("")
            for i in range(0,int(empresas.CantPuntos)):
                print(Fore.LIGHTBLUE_EX+"   "+Fore.LIGHTWHITE_EX+str(i+1)+Fore.LIGHTCYAN_EX+""+PuntoAtención.Nombre)
                PuntoAtención=PuntoAtención.CONTINUAR
            print(Fore.LIGHTBLUE_EX+"   "+Fore.LIGHTWHITE_EX+str(i+2)+Fore.LIGHTCYAN_EX+" Regresar")
            print("")
            print(Fore.LIGHTBLUE_EX+" -.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.- ")
            print(Fore.LIGHTCYAN_EX+"Ingrese el número de punto de atención: ",end="")
            Operación2 = input(Fore.LIGHTWHITE_EX+"")
            try:
                # Si la opción es incorrecta 
                if int(Operación2)<1 or int(Operación2)>int(empresas.CantPuntos)+1:
                    input(Fore.RED+"Ingrese una opción válida.")
                # Si la opción es correcta
                else:
                    # Válidar salida
                    if int(Operación2)==(int(empresas.CantPuntos)+1):
                        salida=1
                    # Guardar id empresa
                    else:
                        return self.IterarPuntos(int(Operación),int(Operación2))
                        #salida=1
            except ValueError:
                input(Fore.RED+"Ingrese un valor numérico.")

    def IterarPuntos(self,Operación,Operación2):
        Buscar=self.Primero
        for i in range(0,Operación-1):
            Buscar=Buscar.SIGUIENTE
        Buscar2=Buscar.PrimerPuntoA
        for j in range(0,Operación2-1):
            Buscar2=Buscar2.CONTINUAR
        return Buscar2 #.IdPuntoA,Buscar2.Nombre

#2 Nodo Empresa
class Empresa():
    def __init__(self, IdEmpresa, Nombre, Abreviatura, CantPuntos,CantServicios):
        self.IdEmpresa=IdEmpresa
        self.Nombre=Nombre
        self.Abreviatura=Abreviatura
        self.CantPuntos=CantPuntos
        self.CantServicios=CantServicios
        self.PrimerPuntoA=None
        self.UltimoPuntoA=None

        # clase servicio
        self.PrimerServicio=None
        self.UltimoServicio=None

        #APUNTADORES lista de empresa
        self.SIGUIENTE=None
        self.ANTERIOR=None
    
    
    def estaVaciaE(self):
        if self.PrimerPuntoA==None:
            return True
        else:
            return False 

    def agregarAListaUltimoE(self,IdPuntoA,Nombre,Direccion,CantEscritorios): 
        nuevo= Puntos_Atencion(IdPuntoA,Nombre,Direccion,CantEscritorios)
        if self.estaVaciaE():
            self.PrimerPuntoA=self.UltimoPuntoA=nuevo
        else:
            temp=self.UltimoPuntoA
            self.UltimoPuntoA=temp.CONTINUAR=nuevo
            self.UltimoPuntoA.RETROCEDER=temp
        self.NullearNodosE()


    def NullearNodosE(self):
        if self.PrimerPuntoA!=None:
            self.PrimerPuntoA.RETROCEDER=NULL
            self.UltimoPuntoA.CONTINUAR=NULL
    
    def recorrerInicio_FinE(self,NoPuntos): #IdPuntoA,Nombre,Direccion,CantEscritorios
        temp1=self.PrimerPuntoA
        for j in range(0,int(NoPuntos)):
            print(Fore.LIGHTBLUE_EX+"   Punto "+str(j+1)+": ")
            print(Fore.LIGHTWHITE_EX+"      Identificacion: "+Fore.LIGHTCYAN_EX+temp1.IdPuntoA)
            print(Fore.LIGHTWHITE_EX+"      Nombre: "+Fore.LIGHTCYAN_EX+temp1.Nombre)
            print(Fore.LIGHTWHITE_EX+"      Dirección: "+Fore.LIGHTCYAN_EX+temp1.Direccion)
            #print(Fore.LIGHTWHITE_EX+"      Cantidad de escritorios: "+Fore.LIGHTCYAN_EX+temp1.CantEscritorios)
            print(Fore.LIGHTWHITE_EX+"      Cantidad de escritorios Inactivos: "+Fore.LIGHTCYAN_EX+str(temp1.CantEscrInactivos))
            print(Fore.LIGHTWHITE_EX+"      Cantidad de escritorios Activos: "+Fore.LIGHTCYAN_EX+str(temp1.CantEscrActivados))
            print(Fore.LIGHTWHITE_EX+"")
            #print(Fore.LIGHTCYAN_EX+"           -----------------"+Fore.LIGHTWHITE_EX+" ESCRITORIOS "+Fore.LIGHTCYAN_EX+"        ")
            temp1.recorrerInicio_FinEscritorio(temp1.CantEscritorios)
            temp1=temp1.CONTINUAR

    def recorrerInicio_FinE2(self,NoPuntos,IDsucursal): #IdPuntoA,Nombre,Direccion,CantEscritorios
        temp1=self.PrimerPuntoA
        for j in range(0,int(NoPuntos)):
            if temp1.IdPuntoA==IDsucursal:
                print(Fore.LIGHTBLUE_EX+"   Punto "+str(j+1)+": ")
                print(Fore.LIGHTWHITE_EX+"      Identificacion: "+Fore.LIGHTCYAN_EX+temp1.IdPuntoA)
                print(Fore.LIGHTWHITE_EX+"      Nombre: "+Fore.LIGHTCYAN_EX+temp1.Nombre)
                print(Fore.LIGHTWHITE_EX+"      Dirección: "+Fore.LIGHTCYAN_EX+temp1.Direccion)
                #print(Fore.LIGHTWHITE_EX+"      Cantidad de escritorios: "+Fore.LIGHTCYAN_EX+temp1.CantEscritorios)
                print(Fore.LIGHTWHITE_EX+"      Cantidad de escritorios Inactivos: "+Fore.LIGHTCYAN_EX+str(temp1.CantEscrInactivos))
                print(Fore.LIGHTWHITE_EX+"      Cantidad de escritorios Activos: "+Fore.LIGHTCYAN_EX+str(temp1.CantEscrActivados))
                print(Fore.LIGHTWHITE_EX+"      Cantidad de clientes: "+Fore.LIGHTCYAN_EX+str(temp1.CantClientes))
                print(Fore.LIGHTWHITE_EX+"")
                print(Fore.LIGHTCYAN_EX+"           -----------------"+Fore.LIGHTWHITE_EX+" ESCRITORIOS "+Fore.LIGHTCYAN_EX+"        ")
                temp1.recorrerInicio_FinEscritorio(temp1.CantEscritorios)
                print(Fore.LIGHTCYAN_EX+"           -----------------"+Fore.LIGHTWHITE_EX+" Clientes "+Fore.LIGHTCYAN_EX+"        ")
                temp1.recorrerInicio_FinCliente(temp1.CantClientes)
            temp1=temp1.CONTINUAR
        
    
    def estaVaciaServicio(self):
        if self.PrimerServicio==None:
            return True
        else:
            return False 

    def agregarAListaUltimoServicio(self,IdServicio,NombreS,MinutosA):
        nuevo= Servicios(IdServicio,NombreS,MinutosA)
        if self.estaVaciaServicio():
            self.PrimerServicio=self.UltimoServicio=nuevo
        else:
            temp=self.UltimoServicio
            self.UltimoServicio=temp.SIG=nuevo
            self.UltimoServicio.ANT=temp
        self.NullearNodosServicio()

    def NullearNodosServicio(self):
        if self.PrimerServicio!=None:
            self.PrimerServicio.ANT=NULL
            self.UltimoServicio.SIG=NULL
    
    def recorrerInicio_FinServicio(self,NoServicios): #IdServicio,NombreS,MinutosA
        temp1=self.PrimerServicio
        for j in range(0,int(NoServicios)):
            print(Fore.LIGHTBLUE_EX+"   Servicio "+str(j+1)+": ")
            print(Fore.LIGHTWHITE_EX+"      Código transacción: "+Fore.LIGHTCYAN_EX+temp1.IdServicio)
            print(Fore.LIGHTWHITE_EX+"      Nombre transacción: "+Fore.LIGHTCYAN_EX+temp1.NombreS)
            print(Fore.LIGHTWHITE_EX+"      Tiempo: "+Fore.LIGHTCYAN_EX+temp1.MinutosA+Fore.LIGHTWHITE_EX+" (min)")
            print(Fore.LIGHTWHITE_EX+"")
            temp1=temp1.SIG

#3 Puntos de atención
class Puntos_Atencion():
    def __init__(self,IdPuntoA,Nombre,Direccion,CantEscritorios):
        self.IdPuntoA=IdPuntoA
        self.Nombre=Nombre
        self.Direccion=Direccion
        self.CantEscritorios=CantEscritorios
        self.CantEscrActivados=0
        self.CantEscrInactivos=0
        self.IdConfig=None
        self.CantClientes=1
        self.CantClientes2=1
        self.CantAtendiendo=0
        
        # clase escritorios Tiempos sumatoria
        self.TiempoMinEspera=1000000000000000 #
        self.TiempoMaxEspera=0 #
        self.TiempoPromedioEspera=0 #
        self.TiempoMinAtencion=100000000000000 #
        self.TiempoMaxAtencion=0 #
        self.TiempoPromAtencion=0 #
        self.TiempoTotal=0 #

        # clase escritorios
        self.PrimerEscritorio=None
        self.UltimoEscritorio=None
        
        # clase clientes
        self.PrimerCliente=None
        self.UltimoCliente=None

        # Apuntadores de Empresa 
        self.CONTINUAR=None
        self.RETROCEDER=None
    

    def estaVaciaEscritorio(self):
        if self.PrimerEscritorio==None:
            return True
        else:
            return False 

    def Crear_Servicio(self):
        temp=self.PrimerCliente
        for i in range(0,int(self.CantClientes)):
            print("Cliente "+str(i))
            print(temp.DPI)
            print(temp.NombreC)
            print(temp.tiempoAtencion)


    def agregarAListaUltimoEscritorio(self,IdEscritorio,IdEncargado, NombreE, Estado):
        nuevo= Escritorios(IdEscritorio,IdEncargado, NombreE, Estado)
        if self.estaVaciaEscritorio():
            self.PrimerEscritorio=self.UltimoEscritorio=nuevo
        else:
            temp=self.UltimoEscritorio
            self.UltimoEscritorio=temp.ESIG=nuevo
            self.UltimoEscritorio.EANT=temp
        self.NullearNodosEscritorio()

    def NullearNodosEscritorio(self):
        if self.PrimerEscritorio!=None:
            self.PrimerEscritorio.EANT=NULL
            self.UltimoEscritorio.ESIG=NULL
    
    def estaVaciaCliente(self):
        if self.PrimerCliente==None:
            return True
        else:
            return False 

    def agregarAListaUltimoCliente(self,DPI,NombreC,tiempoAtencion):
        nuevo= Cliente(DPI,NombreC,tiempoAtencion)
        if self.estaVaciaCliente():
            self.PrimerCliente=self.UltimoCliente=nuevo
        else:
            temp=self.UltimoCliente
            self.UltimoCliente=temp.Csig=nuevo
            self.UltimoCliente.Cant=temp
        self.NullearNodosCliente()

    def eliminar_inicioCliente(self):
        if self.estaVaciaCliente():
            print("ERROR: La lista esta vacia")
        elif self.PrimerCliente==self.UltimoCliente:
            self.PrimerCliente=self.UltimoCliente=None
        else:
            self.PrimerCliente=self.PrimerCliente.Csig
        self.NullearNodosCliente

    def NullearNodosCliente(self):
        if self.PrimerCliente!=None:
            self.PrimerCliente.Cant=NULL
            self.UltimoCliente.Csig=NULL
    
    def recorrerInicio_FinEscritorio(self,NoEscritorios):
        temp1=self.PrimerEscritorio
        for j in range(0,int(NoEscritorios)):
            print(Fore.LIGHTBLUE_EX+ "          Escritorio "+str(j+1)+": ")
            print(Fore.LIGHTWHITE_EX+"              ID Escritorio: "+Fore.LIGHTCYAN_EX+temp1.IdEscritorio)
            print(Fore.LIGHTWHITE_EX+"              Identificación: "+Fore.LIGHTCYAN_EX+temp1.IdEncargado)
            print(Fore.LIGHTWHITE_EX+"              Encargado: "+Fore.LIGHTCYAN_EX+temp1.NombreE)
            print(Fore.LIGHTWHITE_EX+"              Estado: "+Fore.LIGHTCYAN_EX+temp1.Estado)
            print(Fore.LIGHTWHITE_EX+"")
            temp1=temp1.ESIG
    
    def recorrerInicio_FinCliente(self,NoClientes):
        temp1=self.PrimerCliente
        for j in range(0,int(NoClientes)-1):
            print(Fore.LIGHTBLUE_EX+ "          Cliente "+str(j+1)+": ")
            print(Fore.LIGHTWHITE_EX+"              DPI: "+Fore.LIGHTCYAN_EX+temp1.DPI)
            print(Fore.LIGHTWHITE_EX+"              Nombre: "+Fore.LIGHTCYAN_EX+temp1.NombreC)
            print(Fore.LIGHTWHITE_EX+"              Tiempo en ocupar: "+Fore.LIGHTCYAN_EX+str(temp1.tiempoAtencion))
            print(Fore.LIGHTWHITE_EX+"")
            temp1=temp1.Csig
    
#4 Servicios
class Servicios():
    def __init__(self,IdServicio,NombreS,MinutosA):
        self.IdServicio=IdServicio
        self.NombreS=NombreS
        self.MinutosA=MinutosA

        self.SIG=None
        self.ANT=None

#5 Escritorios
class Escritorios():
    def __init__(self,IdEscritorio,IdEncargado, NombreE, Estado):
        self.IdEscritorio=IdEscritorio
        self.IdEncargado=IdEncargado
        self.NombreE=NombreE
        self.Estado=Estado #Activo/Inactivo
        self.Disponible="SI"
        self.TiempoMinAtencion=10000000
        self.TiempoMaxAtencion=0
        self.TiempoPromAntecion=0
        self.TiempoTotal=0
        
        self.NumClientes=0
        self.ClienteNom=None
        self.TiempoActual=0

        self.ESIG=None
        self.EANT=None
         
#6 Nodo Clientes
class Cliente():
    def __init__(self,DPI,NombreC,tiempoAtencion):
        self.DPI=DPI
        self.NombreC=NombreC
        self.tiempoAtencion=tiempoAtencion

        self.PrimerServicio=None
        self.UltimoServicio=None

        self.Csig=None
        self.Cant=None
